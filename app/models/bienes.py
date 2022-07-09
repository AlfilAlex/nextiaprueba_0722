from .. import db
from .user import User


# class Bienes(BaseModel, db.Model):
class Bienes(db.Model):
    __tablename__ = 'bienes'
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
    articulo = db.Column(
        db.String(255),
        nullable=False
    )
    descripcion = db.Column(
        db.String(255),
    )
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # usuario_id = db.relationship("User", back_populates="bienes")
