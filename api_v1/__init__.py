from flask import Blueprint
from flask import Flask

app = Flask(__name__)
api_v1_bp = Blueprint('api_v1', __name__)

from . import routes