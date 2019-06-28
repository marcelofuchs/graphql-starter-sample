from app import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func


class Role(db.Model):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True)
    name = Column(String)
