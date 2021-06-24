import logging
from datetime import datetime

from bard.models.collection import Collection
from bard.app import db

log = logging.getLogger(__name__)


def create_collection(data):
    now = datetime.utcnow()
    collection = Collection.create()
    db.session.commit()
    return collection

