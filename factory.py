from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db_client = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    from config import Config
    app.config.from_object(Config)

    db_client.init_app(app)
    from routes.appointment import appointment_bp
    from routes.home import home_bp
    from routes.services import services_bp
    app.register_blueprint(appointment_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(services_bp)

    return app

