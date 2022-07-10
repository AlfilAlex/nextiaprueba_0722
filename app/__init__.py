from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
migrate = Migrate(compare_type=True)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    with app.app_context():

        from .usuarios.session import user_session
        from .bienes_managment.bienes_managment import bienes_managment

        app.register_blueprint(user_session)
        app.register_blueprint(bienes_managment)
        db.create_all()
        migrate.init_app(app, db)

        return app
