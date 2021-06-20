import logging
from flask import Blueprint, request, current_app

from bard.logic.collections import create_collection

log = logging.getLogger(__name__)
api = Blueprint("api", __name__)


@api.route('/')
def index():
    return "<b>Bard</b>"


@api.route('/create')
def create_collection():
    return "created collection"
