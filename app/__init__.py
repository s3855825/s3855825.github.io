from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__, template_folder='template', static_folder='template/assets')
db = SQLAlchemy(app)
