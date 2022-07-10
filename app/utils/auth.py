from flask import make_response, request, jsonify
from flask import current_app as app
from werkzeug.security import check_password_hash
from datetime import datetime as dt
import jwt
from ..models.user import User
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'}), 401

        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=["HS256"])

            current_user = User.query.filter_by(
                usuario=data['usuario']).first()
        except:
            return jsonify({'message': 'token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorator
