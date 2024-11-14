from flask import Flask, request
import uuid
from flask_smorest import abort
from db import stores, items
import logging
app = Flask(__name__)

# stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


@app.get("/stores")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
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


@app.post("/item")
def create_item():
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

@app.get("/items")  
def get_all_items():
    return {"items":list(items.values())}

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        print(stores[store_id])
        logging.info(str(stores))
        return stores[store_id]
    except Exception:
        return {"message": "Store not found"}, 404
    

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, 
              message = "Item not found")

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item Deleted"}
    except KeyError:
        abort(404, message="Item not found")

@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    # for item in items.values():
    #     if store_id == item[store_id]:
    #         abort(400, message = "The store has some items.Please remove those items inorder to delete the store")
    try:
        del stores[store_id]
        return {"message": "store Deleted"}
    except KeyError:
        abort(404, message="Item not found")