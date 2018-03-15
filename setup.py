"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages

setup(
    description='Sanic Management Blueprint',
    install_requires=['aiofiles', 'httptools', 'sanic',
                      'ujson', 'uvloop', 'websockets', 
                      'async_timeout', 'aiohttp'],
    long_description=open('README.md').read().strip(),
    name='sanic_management_blueprint',
    packages=find_packages(exclude=['tests']),
    py_modules=['sanic_management_blueprint'],
    url='https://github.com/stone-payments/sanic-management-blueprint',
    version='0.1.0',
)
