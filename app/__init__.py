from flask import Flask
from paper import paper
from purpur import purpur
from spigot import spigot



def create_app():
    app = Flask(__name__)

    # Blueprints
    app.register_blueprint(paper)
    app.register_blueprint(purpur)
    app.register_blueprint(spigot)

    return app
