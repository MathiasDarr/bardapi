from bard.models import Collection

def create_collection():
    collection = Collection.create({})
    return collection