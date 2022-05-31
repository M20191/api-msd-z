from flask import Flask
from app.paper import paper
from app.purpur import purpur
from app.spigot import spigot



def create_app():
    app = Flask(__name__)

    # Blueprints
    app.register_blueprint(paper)
    app.register_blueprint(purpur)
    app.register_blueprint(spigot)

    return app
