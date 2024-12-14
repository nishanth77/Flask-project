
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required, get_jwt

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<int:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item
        # demo = ItemModel.query_class()

    @jwt_required()
    def delete(self, item_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            return {"mesage": "Needed a admin privileage to delete an item"}, 401
        
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item Deleted"}
        # raise NotImplementedError()
    @jwt_required()
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)

        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(404, message="The data already exist")
        except SQLAlchemyError as e:
            abort(500, message= str(e))

        return item





# import uuid
# from flask import Flask, request, jsonify
# from flask.views import MethodView
# #from flask_smorest import Blueprint, abort
# from flask_smorest import Blueprint, abort
# from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# from db import db
# from models import ItemModel, StoreModel
# from schemas import ItemSchema,ItemUpdateSchema,StoreSchema

# blp = Blueprint("Items", __name__)

# @blp.route("/item/<string:item_id>")
# class Item(MethodView):
#     @blp.response(200, ItemSchema)
#     def get(self, item_id):
#         try:
#             print("hello world")
#             return items[item_id]
#         except KeyError:
#             abort(404, 
#                 message = "Item not found")

#     def delete(self, item_id):
#         try:
#             del items[item_id]
#             return {"message": "Item Deleted"}
#         except KeyError:
#             abort(404, message="Item not found")
    
#     @blp.arguments(ItemUpdateSchema)
#     @blp.response(200, ItemSchema)
#     def put(self, item_data, item_id):
#         # item_data = request.get_json()
#         # if ("price" not in item_data) or ("name" not in item_data):
#         #     abort(400, message="Bad request!. Check your inputs something is missing out of these name, store_id and price")
#         try:
#             item = items[item_id]
#             item |= item_data
#             return item
#         except KeyError:
#             abort(404, message = "Item not found")

# @blp.route("/item")
# class ItemList(MethodView):
#     @blp.response(200, ItemSchema(many=True))
#     def get(self):
#         return items.values()

#     @blp.arguments(ItemSchema)
#     @blp.response(201, ItemSchema)
#     def post(self,request_data):
#         # request_data = request.get_json()
#         # if ("price" not in request_data) or ("store_id" not in request_data) or ("name" not in request_data):
#         #     abort(400, message="Bad request!. Check your inputs something is missing out of these name, store_id and price")
        
#         # if request_data["store_id"] not in stores:
#         #     return abort(404, message = "Store not found")
        
#         # for item in items.values():
#         #     if request_data["name"] == item["name"] and request_data["store_id"] == item["store_id"]:
#         #         return abort(400, message =f"Item already exists")

#         # item_id = uuid.uuid4().hex
#         # new_item = {**request_data, "id":item_id}
#         # items[item_id] = new_item
#         # return new_item
#         item = ItemModel(**request_data)
#         try:
#             print("into the function post")
#             db.session.add(item)
#             print("after db add statement")
#             db.session.commit()
#             print("after commiting the data")
#         except IntegrityError as e:
#             db.session.rollback()  # Rollback in case of error
#             abort(400, message=str(e.orig))  # Convert the error message to a string
#         except SQLAlchemyError as e:
#             abort(500, message =str(e.orig))
#         # finally:
#         #     db.session.close()
#         return jsonify(item)