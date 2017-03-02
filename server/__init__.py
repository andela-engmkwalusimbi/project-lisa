import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
db = SQLAlchemy(app)

from models import User
