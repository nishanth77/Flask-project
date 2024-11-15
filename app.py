from flask import Flask, request
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

#registering the blueprint
app.config["PROPAGATE_eXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)


# @app.get("/store")
# def get_all_stores():
#     return {"stores": list(stores.values())}


# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         print(stores[store_id])
#         logging.info(str(stores))
#         return stores[store_id]
#     except Exception:
#         return {"message": "Store not found"}, 404
    

# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     if "name" not in store_data:
#         abort(400, message = "Bad Request. Ensure you provide the 'name' in the payload")
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400, "Store already exists")
#     store_id = uuid.uuid4().hex
#     new_store = {**store_data,"id":store_id}
#     stores[store_id] = new_store
#     return new_store, 201


# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     # for item in items.values():
#     #     if store_id == item[store_id]:
#     #         abort(400, message = "The store has some items.Please remove those items inorder to delete the store")
#     try:
#         del stores[store_id]
#         return {"message": "store Deleted"}
#     except KeyError:
#         abort(404, message="Item not found")


# @app.get("/item")  
# def get_all_items():
#     return {"items":list(items.values())}


# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, 
#               message = "Item not found")

# @app.post("/item")
# def create_item():
#     request_data = request.get_json()
#     if ("price" not in request_data) or ("store_id" not in request_data) or ("name" not in request_data):
#         abort(400, message="Bad request!. Check your inputs something is missing out of these name, store_id and price")
    
#     if request_data["store_id"] not in stores:
#         return abort(404, message = "Store not found")
    
#     for item in items.values():
#         if request_data["name"] == item["name"] and request_data["store_id"] == item["store_id"]:
#             return abort(400, message ="Item already exists")

#     item_id = uuid.uuid4().hex
#     item = {**request_data, "id":item_id}
#     items["item_id"] = item
#     return items, 201


# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item Deleted"}
#     except KeyError:
#         abort(404, message="Item not found")


# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.json()
#     if ("price" not in item_data) or ("name" not in item_data):
#         abort(400, message="Bad request!. Check your inputs something is missing out of these name, store_id and price")
#     try:
#         item = items[item_id]
#         item |= item_data
#         return item
#     except KeyError:
#         abort(404, message = "Item not found")

    