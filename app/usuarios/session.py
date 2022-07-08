from flask import request, Blueprint, make_response
from pymysql.err import IntegrityError
from sqlalchemy.exc import IntegrityError, PendingRollbackError
from datetime import datetime as dt
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash

from ..models.user import User
from .. import db

api_prefix = app.config['PREFIX']
user_session = Blueprint('event_profile', __name__, url_prefix=api_prefix)


@user_session.route('/user-registration', methods=['POST'])
def registrate_user():
    nombre = request.form.get('nombre')
    usuario = request.form.get('usuario')
    contrasenia = request.form.get('password')
    secure_con = generate_password_hash(contrasenia, "sha256")

    user = User(created_at=dt.utcnow().isoformat(),
                nombre=nombre,
                usuario=usuario,
                contrasenia=secure_con,)

    try:
        db.session.add(user)
        db.session.commit()
        valid_credentials = True
    except IntegrityError:
        valid_credentials = False
    except Exception as e:
        print(e)
        return make_response({'error': 'Un error interno ocurrió con las credenciales brindadas, revisar'}, 500)

    return make_response({'valid_credentials': valid_credentials})
