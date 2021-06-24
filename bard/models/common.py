import uuid
import secrets
import logging
from sqlalchemy import false
from datetime import datetime, date

from bard.app import db


log = logging.getLogger(__name__)
ENTITY_ID_LEN = 128


def make_textid():
    return uuid.uuid4().hex


def make_token():
    return secrets.token_urlsafe()


def iso_text(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    return obj


def query_like(column, text):
    if text is None or len(text) < 3:
        return false()
    text = text.replace("%", " ").replace("_", " ")
    text = "%%%s%%" % text
    return column.ilike(text)


class IdModel(object):
    id = db.Column(db.Integer(), primary_key=True)


