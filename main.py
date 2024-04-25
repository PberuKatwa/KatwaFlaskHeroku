from flask import Flask,render_template,redirect
from forms import AppointmentForm
from config import Config
from routes.appointment import appointment_bp
from routes.home import home_bp
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(appointment_bp)
    app.register_blueprint(home_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)








