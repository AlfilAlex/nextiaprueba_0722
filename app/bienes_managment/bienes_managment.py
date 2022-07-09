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
bienes_managment = Blueprint(
    'bienes_managment', __name__, url_prefix=api_prefix)


@bienes_managment.route('/user-bienes-registration', methods=['POST'])
def registrate_user_bienes():
    bienes_df = pd.read_csv(request.files['csv_file'])
    # Procesamiento de la información
    # ...
    bienes_df = bienes_df[['id', 'articulo', 'descripcion']]
    # ! FALTA IMPLEMENTAR usuario_id
    bienes = [_get_bien_model(articulo, descripcion)
              for _, articulo, descripcion in bienes_df.to_numpy()]

    try:
        db.session.add_all(bienes)
        db.session.commit()
    except Exception as e:
        print(e)
        make_response(
            {'error': 'No fue posible agregar la información del csv en la base de datos'}, 500)

    return make_response({'no_bienes': len(bienes)})


# ! FALTA IMPLEMENTAR usuario_id
# ! UN ERROR GRAVE CON EL MANY TO ONE EN usuario_id
def _get_bien_model(articulo, descripcion, usuario_id=[User.query.filter_by(id=1).first()]):
    print(articulo, descripcion)
    return Bienes(created_at=dt.utcnow(),
                  articulo=articulo,
                  descripcion=descripcion,
                  usuario_id=usuario_id)  # ! FALTA IMPLEMENTAR
