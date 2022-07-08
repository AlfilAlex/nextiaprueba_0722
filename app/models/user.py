from .. import db
from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    nombre = db.Column(
        db.String(30),
        nullable=False
    )
    usuario = db.Column(
        db.String(30),
        primary_key=True,
    )
    contrasenia = db.Column(
        db.Text(),
        nullable=False
    )
