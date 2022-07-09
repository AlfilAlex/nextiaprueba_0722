"""Se eliminaron primary keys incesesarios de campos

Revision ID: c42f50daff1c
Revises: 6476080f01f7
Create Date: 2022-07-09 11:18:26.023777

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c42f50daff1c'
down_revision = '6476080f01f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bienes', 'descripcion',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('user', 'usuario',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'usuario',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.alter_column('bienes', 'descripcion',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
