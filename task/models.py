from apiserv import db

"""
Database models for Flask-SQLAlchemy
"""

"""
Task DB Model
"""
class Task(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(120))
    body = db.Column(db.Text)
    creation_date = db.Column(db.DateTime)
    completion_date = db.Column(db.DateTime)
    # owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    # category = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(
        self,
        id,
        name,
        # owner, 
        body=None,
        creation_date=None,
        completion_date=None,
        # category=None
    ):
        self.id = id
        self.name = name
        # self.owner = owner
        self.body = body
        self.creation_date = creation_date
        self.completion_date = completion_date
        # self.category = category

    def __repr__(self):
        return '<Task %r>' % self.name
