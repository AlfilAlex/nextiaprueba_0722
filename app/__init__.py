from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# from flask_migrate import Migrate
# migrate = Migrate(compare_type=True)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    with app.app_context():

        from .usuarios.session import user_session

        app.register_blueprint(user_session)
        db.create_all()
        # migrate.init_app(app, db)

        return app
