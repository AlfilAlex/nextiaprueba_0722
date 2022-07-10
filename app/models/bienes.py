from .. import db
from .base_model import BaseModel
from .user import User


class Bienes(BaseModel):
    __tablename__ = 'bienes'
    articulo = db.Column(
        db.String(255),
        nullable=False
    )
    descripcion = db.Column(
        db.String(255),
    )
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
