# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Event Ticket System',
    long_description=readme,
    author='Ben Griffith',
    author_email='bengriffith@outlook.com',
    url='https://github.com/bengriffith/event-ticket-system',
    license=license
)

