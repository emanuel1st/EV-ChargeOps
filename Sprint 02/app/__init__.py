from flask import Flask
from app.database.connection import init_db
from app.routes.dashboard import dashboard_bp
from app.routes.sessions import sessions_bp
from app.routes.invoices import invoices_bp
from app.routes.ai import ai_bp
from app.routes.users import users_bp
from app.routes.chargers import chargers_bp


def create_app():
    app = Flask(__name__, static_folder="../static")

    init_db()

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(sessions_bp)
    app.register_blueprint(invoices_bp)
    app.register_blueprint(ai_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(chargers_bp)

    @app.route("/")
    def home():
        return "<h1>EV ChargeOps</h1><p>Projeto iniciado com sucesso.</p>"

    return app