from unittest import TestCase

from aioresponses import aioresponses

from python_management_blueprint.management import HealthCheck


class TestAppInfo(TestCase):

    def setUp(self):
        HealthCheck.RESOURCES = []

    @aioresponses()
    async def test_check_resources_health(self, mock):
        HealthCheck.register_resource(
            "resource1", "http://mock.com/health-check")

        mock.get("http://mock.com/health-check", status=200,
                 payload={"success": False})

        actual = await HealthCheck.check_resources_health()

        expected = {"resource1": {"success": False}}

        self.assertEqual(actual, expected)

    @aioresponses()
    async def test_check_multiple_resources_health(self, mock):
        HealthCheck.register_resource(
            "resource1", "http://mock.com/health-check")
        mock.get("http://mock.com/health-check", status=200,
                 payload={"success": True})

        HealthCheck.register_resource(
            "resource2", "http://patch.com/health-check")
        mock.get("http://patch.com/health-check", status=200,
                 payload={"success": False, "dependencies": False})

        HealthCheck.register_resource(
            "resource3", "http://dunno.com/health-check")
        mock.get("http://dunno.com/health-check", status=500,
                 payload={"message": "Internal Error"})

        actual = await HealthCheck.check_resources_health()

        expected = {
            "resource1": {"success": True},
            "resource2": {"success": False, "dependencies": False},
            "resource3": {"message": "Internal Error"}
        }

        self.assertEqual(actual, expected)
