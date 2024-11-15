import uuid
from flask import Flask, request
from flask.views import MethodView
#from flask_smorest import Blueprint, abort
from flask_smorest import Blueprint, abort
from db import items, stores

blp = Blueprint("Items", __name__)

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            print("hello world")
            return items[item_id]
        except KeyError:
            abort(404, 
                message = "Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item Deleted"}
        except KeyError:
            abort(404, message="Item not found")
    
    def put(self, item_id):
        item_data = request.json()
        if ("price" not in item_data) or ("name" not in item_data):
            abort(400, message="Bad request!. Check your inputs something is missing out of these name, store_id and price")
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message = "Item not found")

@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items":list(items.values())}
        
    def post(self):
        request_data = request.get_json()
        if ("price" not in request_data) or ("store_id" not in request_data) or ("name" not in request_data):
            abort(400, message="Bad request!. Check your inputs something is missing out of these name, store_id and price")
        
        if request_data["store_id"] not in stores:
            return abort(404, message = "Store not found")
        
        for item in items.values():
            if request_data["name"] == item["name"] and request_data["store_id"] == item["store_id"]:
                return abort(400, message ="Item already exists")

        item_id = uuid.uuid4().hex
        item = {**request_data, "id":item_id}
        items["item_id"] = item
        return items, 201