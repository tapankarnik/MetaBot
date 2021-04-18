from flask import Flask
from config import Config
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
#app.config.from_object(Config)
app.config['SECRET_KEY'] = SECRET_KEY

from app import routes

app.run(debug=True)
