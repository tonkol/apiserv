from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Recreate database

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

# Just to make sure table entries are dropped
db.reflect()
db.session.commit()
db.drop_all()
db.create_all()
