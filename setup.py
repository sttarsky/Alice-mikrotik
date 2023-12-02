
from setuptools import setup, find_packages

setup(
    name='myproject',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'netmiko',
        'flask'
    ],
    author='John Doe',
    description='My awesome project',
    license='MIT'
)
