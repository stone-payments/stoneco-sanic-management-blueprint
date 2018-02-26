"""A module that creates a Sanic App and registers its blueprints."""
from sanic import Sanic
from python_management_blueprint.management import setup_blueprint


def create_api():
    """Function that returns a Sanic API with its blueprints registered."""
    api = Sanic()
    api.blueprint(setup_blueprint())
    return api
