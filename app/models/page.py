
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import Base

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True)
    linkedin_page_id = Column(String, unique=True)
    name = Column(String)
    industry = Column(String)
    followers_count = Column(Integer)
    description = Column(Text)

    posts = relationship("Post", back_populates="page", cascade="all, delete")
