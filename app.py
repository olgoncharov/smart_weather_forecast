from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration())
db = SQLAlchemy(app)
cache = Cache(app)