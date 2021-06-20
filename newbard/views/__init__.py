from bard.views.api import api
from bard.views.base_api import blueprint as base_api

def mount_app_blueprints(app):
    app.register_blueprint(api)
    app.register_blueprint(base_api)
