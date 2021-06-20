import os


APP_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = 'postgresql://bard:bard@postgres:5432/bard'
SQLALCHEMY_TRACK_MODIFICATIONS = False
ALEMBIC_DIR = os.path.join(APP_DIR, "migrate")