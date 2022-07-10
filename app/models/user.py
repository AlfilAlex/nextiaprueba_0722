from .. import db
# from .base_model import BaseModel
# from .bienes import Bienes
from sqlalchemy import ForeignKey
from .base_model import BaseModel


class User(BaseModel):
    # class User(db.Model):
    __tablename__ = 'user'
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
    bienes = db.relationship("Bienes")
