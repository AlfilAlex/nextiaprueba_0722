from flask import request, Blueprint, make_response
from pymysql.err import IntegrityError
from sqlalchemy.exc import IntegrityError
from datetime import datetime as dt
from flask import current_app as app
from sqlalchemy import exc

from ..models.bienes import Bienes
from .. import db
from ..utils.auth import token_required

import pandas as pd
import numpy as np


api_prefix = app.config['PREFIX']
bienes_managment = Blueprint(
    'bienes_managment', __name__, url_prefix=api_prefix)


@bienes_managment.route('/csv-bienes-registration', methods=['POST'])
@token_required
def user_csv_post_bienes(current_user):
    bienes_df = pd.read_csv(request.files['csv_file'])
    try:
        bienes_df = bienes_df[['id', 'articulo', 'descripcion']]
    except KeyError:
        return make_response({'error': 'Nombre de columnas no invalidos en el csv. Las columnas deben ser: id, articulo, descripcion'}, 400)
    else:
        # ...Procesamiento de la información...
        pass

    bienes = [_get_bien_model(articulo, descripcion, current_user.id)
              for _, articulo, descripcion in bienes_df.to_numpy()]

    try:
        db.session.add_all(bienes)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return make_response(
            {'error': 'No fue posible agregar la información del csv en la base de datos debido a un error con el ORM'}, 500)
    except Exception as e:
        print(e)
        return make_response(
            {'error': 'Un error fatal ocurrió durante la operación en la base de datos'}, 500)

    return make_response({'no_bienes': len(bienes), 'user_info': _get_user_info(current_user)})


@bienes_managment.route('/bienes-managment', methods=['POST'])
@token_required
def bienes_registration(current_user):
    articulo = request.form.get('articulo')
    descripcion = request.form.get('descripcion')

    usuario_id = current_user.id
    bien = Bienes(created_at=dt.utcnow().isoformat(),
                  articulo=articulo,
                  descripcion=descripcion,
                  usuario_id=usuario_id)
    try:
        db.session.add(bien)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return make_response({'succes': False, 'error': 'Posible duplicado'}, 403)
    except Exception as e:
        return make_response({'succes': False, 'error': 'Un error interno ocurrió con las credenciales brindadas, revisar'}, 500)

    return make_response({'succes': True, 'bien': {'articulo': articulo, 'id': bien.id}, 'user_info': _get_user_info(current_user)}, 200)


@bienes_managment.route('/bienes-managment/buscar', methods=['GET'])
@token_required
def bienes_read(current_user):
    usuario_id = current_user.id

    bien_ids = request.args.get('bien_id')
    bien_ids = bien_ids.split(',')

    bienes = [Bienes.query.get(bien_id) for bien_id in bien_ids]
    bienes_in_db = [bien_id for bien_id in bienes if bien_id is not None]
    bienes_info = [_get_bien_info(bien) for bien in bienes_in_db]

    if not bienes_info:
        succes = False
        message = {'error': f'No existen bienes con id: {bien_ids}'}
        status = 500
    else:
        succes = True
        message = {'bienes': bienes_info}
        status = 200

    return make_response({'succes': succes, 'message': message, 'user_info': _get_user_info(current_user)}, status)


@bienes_managment.route('/bienes-managment/<int:bien_id>', methods=['PUT'])
@token_required
def bienes_update(current_user, bien_id):
    bien = Bienes.query.filter_by(id=bien_id)
    bien_modificado = bien.first()
    if bien_modificado:
        cambios_por_columna = request.get_json()
        cambios_por_columna['updated_at'] = dt.utcnow().isoformat()
        try:
            bien.update(cambios_por_columna)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            return make_response({'succes': False, 'error': 'Posible duplicado'}, 403)

        return make_response({'bien': _get_bien_info(bien_modificado), 'user_info': _get_user_info(current_user)}, 200)

    else:
        return make_response(
            {'error': f'El bien con id {bien_id} puede no existir'}, 403)


@bienes_managment.route('/bienes-managment/<bien_id>', methods=['DELETE'])
@token_required
def bienes_delete(current_user, bien_id):
    usuario_id = current_user.id
    bien = Bienes.query.get(bien_id)
    if not bien:
        succes = False
        status = 403
    else:
        try:
            db.session.delete(bien)
            db.session.commit()
            succes = True
            status = 200
        except exc.SQLAlchemyError:
            db.session.rollback()
            return make_response({'succes': False, 'error': 'Posible duplicado'}, 403)

    return make_response({'succes': succes, 'user_info': _get_user_info(current_user)}, status)


def _get_bien_model(articulo, descripcion, usuario_id):
    if not isinstance(descripcion, str) and np.isnan(descripcion):
        descripcion = None
    return Bienes(created_at=dt.utcnow().isoformat(),
                  articulo=articulo,
                  descripcion=descripcion,
                  usuario_id=usuario_id)


def _get_bien_info(bien):
    return {'id': bien.id, 'article': bien.articulo,
            'descripcion': bien.descripcion, 'user_author_id': bien.usuario_id}


def _get_user_info(user):
    return {'nombre': user.nombre, 'id': user.id, 'bienes': [bien.id for bien in user.bienes]}
