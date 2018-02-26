"""Module to define classes to retrieve app health"""
import aiohttp
import asyncio
import async_timeout


async def fetch(session, url):
    async with async_timeout.timeout(30):
        async with session.get(url) as response:
            return await response.json()


async def execute_request(url):
    async with aiohttp.ClientSession() as session:
        json = await fetch(session, url)
        return json


class HealthCheck(object):
    """Class to define methods to manage app health"""

    RESOURCES = []

    @classmethod
    def register_resource(cls, name, url):
        """Method to register a resource necessary to the app

        Args:
            name (string): Name of system to check health
            url (string): Url of system to check health
        """

        cls.RESOURCES.append({name: url})

    @classmethod
    def check_resources_health(cls):
        url_list = [list(rec.values())[0]
                    for rec in cls.RESOURCES]

        name_list = [list(rec.keys())[0]
                     for rec in cls.RESOURCES]

        loop = asyncio.get_event_loop()
        resp = loop.run_until_complete(asyncio.gather(
            *[execute_request(url) for url in url_list]
        ))
        return dict(zip(name_list, resp))
