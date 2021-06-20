import logging
from functools import lru_cache
from flask import Blueprint, request, current_app, jsonify
import os

blueprint = Blueprint("base_api",__name__)
log = logging.getLogger(__name__)


@blueprint.route("/api/2/metadata")
def metadata():
    """
    Get operation metadata for the frontend
    """
    request.rate_limit = None

    return jsonify({"metadata":"bard"})
