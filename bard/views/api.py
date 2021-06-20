import logging
from flask import Blueprint, request, current_app

log = logging.getLogger(__name__)
api = Blueprint("api", __name__)

@api.route('/')
def index():
    return "<b>Bard</b>"
