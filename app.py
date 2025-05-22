from flask import Flask
from flask_cors import CORS
from config import Config
from database import db
from controllers.reserva_route import reserva_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    app.register_blueprint(reserva_bp, url_prefix="/reservas")

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
