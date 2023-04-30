from distutils.command.config import config
from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine


# the __name__ special variable to identify the module being rendered
app = Flask(__name__)
app.config.from_object(config)
app.config['SECRET_KEY'] = 'any secret string'

db = MongoEngine()
db.init_app(app)

from application import routes
