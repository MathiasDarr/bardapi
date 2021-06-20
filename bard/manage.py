from flask.cli import FlaskGroup
import click
from api.app import create_app


import logging

@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    "Server side command line"