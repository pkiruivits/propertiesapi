#from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class propdetail(Base):
    __tablename__ = "propdetails"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String, unique=True, index=True)
    description = sa.Column(sa.String)
    specification = sa.Column(sa.String)
    architects = sa.Column(sa.String,nullable=True)
    area = sa.Column(sa.Integer,nullable=True)
    year = sa.Column(sa.Integer,nullable=True)
    manufacturers = sa.Column(sa.String,nullable=True)
    updated_at = sa.Column(sa.DateTime(), onupdate=datetime.now())
    created_at = sa.Column(sa.DateTime(), default=datetime.now())

    images = relationship("Images", back_populates="product")

class Images(Base):
    __tablename__ = "images"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    property_id = sa.Column(sa.Integer, sa.ForeignKey("propdetails.id"))
    image_url = sa.Column(sa.String)
    updated_at = sa.Column(sa.DateTime(), onupdate=datetime.now())
    created_at = sa.Column(sa.DateTime(), default=datetime.now())

    product = relationship("propdetail", back_populates="images")
