from flask import Blueprint

api = Blueprint('api', __name__)

from application.api import (
    user
)
