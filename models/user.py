from datetime import datetime, timezone
from extensions import db
from models.blog import Blog


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(25), nullable=False, unique=True)
  password = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
  email = db.Column(db.String(120), unique=True, nullable=False)


  blogs = db.relationship('Blog', back_populates='author', cascade="all, delete-orphan")

  def __repr__(self) -> str:
    return f"Task {self.id}"
  