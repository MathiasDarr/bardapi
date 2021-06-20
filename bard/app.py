import logging
from flask import Flask, request

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cors import CORS


from bard import config

NONE = "'none'"
log = logging.getLogger(__name__)

db = SQLAlchemy()
migrate = Migrate()

def create_app(configurations={}):
    app = Flask("api")


    migrate.init_app(app, db, directory=config.ALEMBIC_DIR)
    db.init_app(app)

    CORS(
        app,
        resources=r"/api/*",
        origins="*",
        supports_credentials=True,
    )

    from bard.views import mount_app_blueprints

    mount_app_blueprints(app)
    return app
