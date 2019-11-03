from flask import Blueprint
# llamado, el nombre de este archivo y con prefijo auth.
auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views
