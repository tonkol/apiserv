from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# TODO:
# Think about this approach?
# http://flask-sqlalchemy.pocoo.org/2.1/contexts/

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

from api import views # Blueprint
from api.views import api as api_blueprint

app.register_blueprint(api_blueprint)
