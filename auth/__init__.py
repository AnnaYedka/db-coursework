from flask import Blueprint

bp = Blueprint('auth', __name__)

from . import routes
from .routes import admin_required
