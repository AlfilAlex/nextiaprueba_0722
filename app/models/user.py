from .. import db
from .base_model import BaseModel
from sqlalchemy import ForeignKey


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
    bien_id = db.Column(db.Integer, ForeignKey("bienes.id"))
    child = db.relationship("Bienes", back_populates="user")
