"""Resource to manage api settings"""
from sanic.response import json
from sanic import Blueprint

from .app_info import AppInfo


def setup_blueprint():
    """Creates a blueprint and register its routes"""
    blueprint = Blueprint('Management')
    blueprint.add_route(app_info, '/management/app-info', methods=['GET'])
    return blueprint


async def app_info(request):
    """Returns general informations about the application"""
    return json(AppInfo.app_info())
