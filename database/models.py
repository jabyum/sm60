from database import Base
from sqlalchemy import (Column, Integer, String,
                        ForeignKey, DateTime)
from sqlalchemy.orm import relationship
from datetime import datetime
import pytz
tashkent_timezone = pytz.timezone("Asia/Tashkent")
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    city = Column(String, nullable=True)
    birthday = Column(String, nullable=True)
    password = Column(String)
    reg_date = Column(DateTime, default=datetime.now(tashkent_timezone))
    post_fk = relationship("Post", back_populates="users_fk")
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String, nullable=True)
    post_date = Column(DateTime, default=datetime.now(tashkent_timezone))
    hashtags = Column(String, ForeignKey("hashtags.id"))
    hashtags_fk = relationship("Hashtag", lazy="subquery")
    users_fk = relationship(User, lazy="subquery", back_populates="post_fk",
                            cascade="all, delete", passive_deletes=True)
class Hashtag(Base):
    __tablename__ = "hashtags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    hashtag_name = Column(String, unique=True)
    reg_date = Column(DateTime, default=datetime.now(tashkent_timezone))
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.now(tashkent_timezone))
    author = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post_fk = relationship(Post, lazy="subquery")
    user_fk = relationship(User, lazy="subquery")
class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)
    path = Column(String)
    user_fk = relationship("User", lazy='subquery')
    post_fk = relationship("Post", lazy='subquery')