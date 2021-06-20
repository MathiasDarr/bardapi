import logging
from flask import Flask, request

from flask_cors import CORS

NONE = "'none'"
log = logging.getLogger(__name__)


def create_app(config={}):
    app = Flask("api")

    CORS(
        app,
        resources=r"/api/*",
        origins="*",
        supports_credentials=True,
    )

    from bard.views import mount_app_blueprints

    mount_app_blueprints(app)
    return app
