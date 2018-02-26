from unittest import TestCase
# from unittest.mock import patch, MagicMock

from python_management_blueprint.management import HealthCheck


class TestAppInfo(TestCase):

    def setUp(self):
        HealthCheck.RESOURCES = []

    def test_check_resources_health(self):
        HealthCheck.register_resource(
            'name1', 'http://localhost:5001/health-check')
        HealthCheck.register_resource(
            'name2', 'http://localhost:5959/health-check')

        HealthCheck.check_resources_health()

        self.assertFalse(True)
