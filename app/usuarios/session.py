from flask import request, make_response, current_app, jsonify
from pymysql.err import IntegrityError
from sqlalchemy.exc import IntegrityError, PendingRollbackError
from datetime import datetime as dt
from flask import current_app as app
from flask import Blueprint

api_prefix = current_app.config['PREFIX']
user_session = Blueprint('event_profile', __name__, url_prefix=api_prefix)
