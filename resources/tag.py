import uuid
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from schemas import TagSchema, TagAndItemSchema
from models import StoreModel, TagModel, ItemModel

blp = Blueprint("Tags", "tags", description="operations on tag models", url_prefix="/api/v1")

@blp.route("/store/<int:store_id>/tag")
class TagsInStore(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()

    @blp.arguments(TagSchema)
    @blp.response(201, TagSchema)
    def post(self, tag_data, store_id):
        if TagModel.query.filter(TagModel.store_id==store_id, TagModel.name==tag_data['name']).first():
            abort(400, message="the tag with this name is already added in the store")
        tag = TagModel(**tag_data, store_id=store_id)
        try:
            db.session.add(tag)
            db.session.commit()

        except SQLAlchemyError as e:
            abort(500, message=str(e))
        
        return tag

@blp.route("/items/<int:item_id>/tag/<int:tag_id>")
class LinkTagsToItem(MethodView):
    @blp.response(200, TagAndItemSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.append(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message = "An Error occured while inserting the data")
        return tag

    @blp.response(200, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An Error occured while deleting the data")
        return {"message" : "Tag removed from the tag", "item":item, "tag":tag}

@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag
    
    @blp.response(202, description="Deletes a tag if no items tagged with it")
    @blp.alt_response(404, description="Tag not found")
    @blp.alt_response(400, description="Returned if the Tag is linked to an item")
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)

        if not tag.items().all():
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Tag deleted successfully"}
        abort(400, message="Tag is linked to an item, unable to delete it")
        


