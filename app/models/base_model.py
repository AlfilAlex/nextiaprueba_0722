from .. import db


class BaseModel:
    __tablename__ = 'base'
    id = db.Column(
        primary_key=True,
    )
    created_at = db.Column(
        db.DateTime,
    )
    updated_at = db.Column(
        db.DateTime,
    )
