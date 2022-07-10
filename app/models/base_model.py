from .. import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    created_at = db.Column(
        db.DateTime,
    )
    updated_at = db.Column(
        db.DateTime,
    )
