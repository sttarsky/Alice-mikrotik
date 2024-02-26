
from setuptools import setup, find_packages

setup(
    name='myproject',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'netmiko',
        'fastapi',
        'uvicorn',
        'setuptools'
    ],
    author='John Doe',
    description='My awesome project',
    license='MIT'
)
