from extensions import db 
from datetime import datetime, timezone

class Blog(db.model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), nullable=False)
  content = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
  is_published = db.Column(db.Boolean, default=False)
  
   # Foreign key to link the blog to its author
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship back to User
  author = db.relationship('User', back_populates='blogs')

  def __repr__(self):
      
        return f"<Blog {self.title[:50]} by User {self.author_id}>"