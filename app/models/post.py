from sqlalchemy import Column, Integer, Text, ForeignKey
from app.models.base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    likes = Column(Integer)
    page_id = Column(Integer, ForeignKey("pages.id"))
