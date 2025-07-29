import os
from flask import Flask
from dotenv import load_dotenv
from app.config import Config
from app.extensions import db, login_manager, bcrypt, migrate, mail
import stripe

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    # Initialisation des extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Clé Stripe
    app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY')
    stripe.api_key = app.config['STRIPE_SECRET_KEY']

    # Import et enregistrement des blueprints
    from app.routes.routes import main
    from app.auth.routes import auth_bp
    from app.admin.routes import admin_bp
    from app.errors.handlers import errors
    from app.routes.paiement import paiement_bp
    from app.routes.stripe import stripe_bp

    app.register_blueprint(main)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(errors)
    app.register_blueprint(paiement_bp)
    app.register_blueprint(stripe_bp)

    return app
