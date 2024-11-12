from flask import Flask, request
import uuid
from flask_smorest import abort
from db import stores, items

app = Flask(__name__)

# stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


@app.get("/stores")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data,"id":store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.post("/item")
def create_item():
    request_data = request.get_json()
    if request_data["store_id"] not in stores:
        return abort(404, message = "Store not found")
    
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
        return stores["store_id"]
    except Exception:
        return {"message": "Store not found"}, 404
    

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items["item_id"]
    except KeyError:
        abort(404, 
              message = "Item not found")
