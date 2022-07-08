from io import StringIO

from flask import request, Blueprint, make_response
from pymysql.err import IntegrityError
from sqlalchemy.exc import IntegrityError, PendingRollbackError
from datetime import datetime as dt
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash

from ..models.user import User
from ..models.bienes import Bienes
from .. import db
import pandas as pd

api_prefix = app.config['PREFIX']
user_session = Blueprint('event_profile', __name__, url_prefix=api_prefix)


@user_session.route('/user-bienes-registration', methods=['POST'])
def registrate_user_bienes():
    bienes_df = pd.read_csv(request.files['data_file'])
