import uuid
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from db import db
import logging
from schemas import StoreSchema
from models import StoreModel


blp = Blueprint("Stores", __name__,description="operations on stores model", url_prefix="/api/v1")

@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            # print(stores[store_id])
            # logging.info(str(stores))
            return StoreModel.query.get_or_404(store_id)
        except Exception:
            return {"message": "Store not found"}, 404

    @jwt_required()
    def delete(self, store_id):
        try:
            del_store = StoreModel.query.get_or_404(store_id)
            # raise NotImplementedError()
            db.session.delete(del_store)
            db.session.commit()
            return {"message":"store deleted successfully"}
        except KeyError:
            abort(404, message="Item not found")

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @jwt_required()
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self,store_data):
        # store_data = request.get_json()
        # if "name" not in store_data:
        #     abort(400, message = "Bad Request. Ensure you provide the 'name' in the payload")
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(404, message="The data already exist")
        except SQLAlchemyError as e:
            abort(500, message= str(e))
        return store