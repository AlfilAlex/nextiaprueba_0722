from .. import db
from .base_model import BaseModel


class Bienes(BaseModel):
    __tablename__ = 'bienes'
    articulo = db.Column(
        db.String(255),
        nullable=False
    )
    descripcion = db.Column(
        db.String(255),
        primary_key=True,
    )
    usuario_id = db.relationship("User", back_populates="bienes")
