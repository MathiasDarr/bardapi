from flask import Blueprint, request, jsonify
import logging
from bard.logic.collections import create_collection
from bard.app import db

log = logging.getLogger(__name__)

blueprint = Blueprint("collections_api", __name__)

@blueprint.route("/", methods=["GET"])
def index():
    """
    List of collections
    """
    return "hello"

@blueprint.route("/create", methods=["POST", "PUT"])
def create():
    return "not hot reloaddf dfad "
    # request_data = request.get_json()
    #
    # # summary = request_data['summary']
    # label = request_data['label']
    #
    # collection = create_collection(data=request_data)
    # resp_dictionary = {
    #     "collection_id": collection.id,
    #     "label": collection.label
    # }
    # return jsonify(resp_dictionary)

