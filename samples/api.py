"""A module that creates a Sanic App and registers its blueprints."""
from sanic import Sanic
import requests

from sanic_management_blueprint.management import setup_blueprint, AppInfo, HealthCheck

def sample_check_resource():
    return True

    
    
def create_api():
    """Function that returns a Sanic API with its blueprints registered."""
    api = Sanic()
    api.blueprint(setup_blueprint())
    AppInfo.register_resource(sample_check_resource)
    HealthCheck.register_resource('httpbin', 'https://httpbin.org/get')
    return api
