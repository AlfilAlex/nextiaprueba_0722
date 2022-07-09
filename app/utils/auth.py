from flask import make_response, request, jsonify
from flask import current_app as app
from werkzeug.security import check_password_hash
from datetime import datetime as dt
import jwt
from ..models.user import User
from functools import wraps

# @app.route('/login', methods=['GET', 'POST'])
# def login_user():

#     auth = request.authorization

#     if not auth or not auth.username or not auth.password:
#         return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

#     user = User.query.filter_by(name=auth.username).first()

#     if check_password_hash(user.password, auth.password):
#         token = jwt.encode(
#             {'usuario': user.usuario, 'contrasenia': user.contrasenia}, app.config['SECRET_KEY'])
#         return jsonify({'token': token.decode('UTF-8')})

#     return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(
                usuario=data['usuario']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator
