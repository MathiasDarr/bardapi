from bard.app import db


class IdModel(object):
    id = db.Column(db.Integer(), primary_key=True)


class Collection(IdModel):
    label = db.Column(db.Unicode)
    def touch(self):
        db.session.add(self)

    def update(self, data):
        self.label = data.get("label", self.label)
        self.touch()
        db.session.flush()
    @classmethod
    def create(cls, data):
        collection = cls()
        return collection
# class Document(IdModel):
