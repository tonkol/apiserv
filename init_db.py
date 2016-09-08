from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Recreate database

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
db.drop_all()
db.create_all()
