"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages

setup(
    description='Python Management Blueprint',
    install_requires=['aiofiles', 'httptools', 'sanic',
                      'ujson', 'uvloop', 'websockets'],
    long_description=open('README.md').read().strip(),
    name='python_management_blueprint',
    packages=find_packages(exclude=['tests']),
    py_modules=['python_management_blueprint'],
    url='https://github.com/stone-payments/python-management-blueprint',
    version='0.0.1',
)
