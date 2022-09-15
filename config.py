from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Flask Config
app = Flask(__name__)
app.config.from_object("settings")

# Database
db = SQLAlchemy(app)

# Marshmallow
json = Marshmallow(app)