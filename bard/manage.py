from flask.cli import FlaskGroup
import click
from bard.app import create_app
from bard.migration import upgrade_system, destroy_db
from bard.app import create_app

import logging

log = logging.getLogger(__name__)

@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    "Server side command line"


@cli.command()
def upgrade():
    """Create or upgrade the search index and database."""
    upgrade_system()