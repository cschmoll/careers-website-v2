from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()

class Jobs(Base, SerializerMixin):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    salary = Column(Integer)
    currency = Column(String)
    responsibilities = Column(String)
    requirements = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    location = Column(String)
