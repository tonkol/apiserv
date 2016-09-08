from apiserv import db
import time, datetime
"""
Database models for Flask-SQLAlchemy
"""

"""
Task DB Model
"""
class Task(db.Model):
    id = db.Column(db.String, primary_key=True)
    text = db.Column(db.String(120))
    body = db.Column(db.Text)
    completed = db.Column(db.Boolean)
    createdAt = db.Column(db.DateTime)
    completedAt = db.Column(db.DateTime)
    # owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    # category = db.Column(db.Integer, db.ForeignKey('category.id'))

    def _convert_to_DateTime(self, dt):
        return datetime.datetime.fromtimestamp(dt)

    def __init__(
        self,
        id,
        text,
        completed,
        # owner, 
        body=None,
        createdAt=None,
        completedAt=None,
        # category=None
    ):
        self.id = id
        self.text = text
        # self.owner = owner
        self.body = body
        if createdAt:
            createdAt_dt = self._convert_to_DateTime(createdAt)
            self.createdAt = createdAt_dt
        if completedAt:
            completedAt_dt = self._convert_to_DateTime(completedAt)
            self.completedAt = completedAt_dt
        
        self.completed = completed
        # self.category = category

    def __repr__(self):
        return '<Task %r>' % self.name
