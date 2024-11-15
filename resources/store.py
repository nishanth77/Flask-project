import uuid
from flask import Flask, request
from flask.views import MethodView
#from flask_smorest import Blueprint, abort
from flask_smorest import Blueprint, abort
from db import stores
import logging
blp = Blueprint("Stores", __name__)

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            print(stores[store_id])
            logging.info(str(stores))
            return stores[store_id]
        except Exception:
            return {"message": "Store not found"}, 404

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "store Deleted"}
        except KeyError:
            abort(404, message="Item not found")

@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}
        
    def post(self):
        store_data = request.get_json()
        if "name" not in store_data:
            abort(400, message = "Bad Request. Ensure you provide the 'name' in the payload")
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, "Store already exists")
        store_id = uuid.uuid4().hex
        new_store = {**store_data,"id":store_id}
        stores[store_id] = new_store
        return new_store, 201