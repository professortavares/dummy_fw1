from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='dummyfw',
    version='1.0.1',
    packages=['dummyfw'],
    url='',
    license='',
    author='leonardo',
    author_email='',
    description='',
    install_requires=required
)
