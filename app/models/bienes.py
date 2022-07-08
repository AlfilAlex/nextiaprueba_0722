from .. import db
# from .base_model import BaseModel


# class Bienes(BaseModel, db.Model):
class Bienes(db.Model):
    __tablename__ = 'bienes'
    # ?
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    created_at = db.Column(
        db.DateTime,
    )
    updated_at = db.Column(
        db.DateTime,
    )
    # ?
    articulo = db.Column(
        db.String(255),
        nullable=False
    )
    descripcion = db.Column(
        db.String(255),
        primary_key=True,
    )
    usuario_id = db.relationship("User", back_populates="bienes")
