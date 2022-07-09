from .. import db
# from .base_model import BaseModel
# from .bienes import Bienes
from sqlalchemy import ForeignKey


# class User(BaseModel, db.Model):
class User(db.Model):
    __tablename__ = 'user'
    # ?
    id = db.Column(
        db.Integer,
        primary_key=True,
        # autoincrement=True
    )
    created_at = db.Column(
        db.DateTime,
    )
    updated_at = db.Column(
        db.DateTime,
    )
    # ?
    nombre = db.Column(
        db.String(30),
        nullable=False
    )
    usuario = db.Column(
        db.String(30),
        unique=True
    )
    contrasenia = db.Column(
        db.Text(),
        nullable=False
    )
    # bien_id = db.Column(db.Integer, ForeignKey(Bienes.id), nullable=True)
    bienes = db.relationship("Bienes")
