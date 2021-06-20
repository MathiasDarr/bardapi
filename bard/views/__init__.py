from bard.views.api import blueprint as collections_api

def mount_app_blueprints(app):
    app.register_blueprint(collections_api)
