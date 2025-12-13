from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import Base

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    linkedin_page_id = Column(String, unique=True, index=True)
    name = Column(String)
    url = Column(String)
    industry = Column(String)
    followers_count = Column(Integer)
    description = Column(Text)

    # relationship to posts
    posts = relationship("Post", back_populates="page", cascade="all, delete")
