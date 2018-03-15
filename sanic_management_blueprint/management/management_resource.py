"""Resource to manage api settings"""
from sanic.response import json
from sanic import Blueprint

from .app_info import AppInfo
from .health_check import HealthCheck


def setup_blueprint():
    """Creates a blueprint and register its routes"""
    blueprint = Blueprint('Management')
    blueprint.add_route(app_info, '/management/app-info', methods=['GET'])
    blueprint.add_route(health_check, '/management/health-check',
                        methods=['GET'])
    return blueprint


async def app_info(request):
    """Returns general informations about the application"""
    return json(AppInfo.app_info())


async def health_check(request):
    """Returns general informations about the health of the application"""
    info = AppInfo.app_info()
    info['Components'] = await HealthCheck.check_resources_health()
    return json(info)
