from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from application.flask_config import Config

db = SQLAlchemy()

def create_app(flask_config):
    app = Flask(__name__)
    Config.init_app(app)
    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from application.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    @app.route('/')
    def hello():
        return "hello, world"

    return app
