from app import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func


class Department(db.Model):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
