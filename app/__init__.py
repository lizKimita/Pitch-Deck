from flask import Flask
from app import DevConfig
from flask_bootstrap import Bootstrap
from app import views
from app import error

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
