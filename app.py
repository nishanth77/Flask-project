from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from db import db
import models
from blocklist import BLOCKLIST
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)
    
    app.config["JWT_SECRET_KEY"] = "193167227067625722259894652244295329254"
    jwt = JWTManager(app)    

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        #need to implement the fetching of admin criteria frm the database
        if True:
            return {"is_admin": True}
        else:
            return {"is_admin": False}

    #decorator for handling token expiration

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (jsonify({"message":"Token has been revoked", "error":"Token revoked"}), 401)
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (jsonify({"message":"The token is expired.", "error":"Token expired"}), 401)
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (jsonify({"message":"Signature verification failed.", "error":"Invalid token"}), 401)
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (jsonify({"message":"Request does not contain an access token.", "error":"Missing token"}), 401)

    #commenting this as used alembic for migration
    # with app.app_context():
    #     db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)
    return app