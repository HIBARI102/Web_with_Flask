import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Package-level DB instance (initialized in create_app)
db = SQLAlchemy()
# Login manager
login_manager = LoginManager()


def create_app(config_object=None):
    """Application factory for StayFix.

    Creates the Flask app, initializes extensions, registers blueprints,
    and exposes a simple CLI command to initialize the SQLite database.
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("STAYFIX_SECRET", "dev"),
        SQLALCHEMY_DATABASE_URI="sqlite:///"
        + os.path.join(app.instance_path, "stayfix.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if config_object:
        app.config.from_object(config_object)

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # add template helpers for language switching
    try:
        from .utils import register_language_helpers

        register_language_helpers(app)
    except Exception:
        pass

    # Import models so they are registered with SQLAlchemy and wire user loader
    with app.app_context():
        try:
            from . import models  # noqa: F401

            @login_manager.user_loader
            def load_user(user_id):
                try:
                    from .models import User

                    return User.query.get(int(user_id))
                except (Exception, TypeError, ValueError):
                    return None

        except Exception:
            pass

    # Register blueprints (safe to ignore import errors while scaffolding)
    try:
        from .routes.main import main_bp

        app.register_blueprint(main_bp)
    except Exception:
        pass

    try:
        from .routes.tickets import tickets_bp

        app.register_blueprint(tickets_bp, url_prefix="/tickets")
    except Exception:
        pass

    try:
        from .routes.rooms import rooms_bp

        app.register_blueprint(rooms_bp, url_prefix="/rooms")
    except Exception:
        pass

    try:
        from .routes.auth import auth_bp

        app.register_blueprint(auth_bp, url_prefix="/auth")
    except Exception:
        pass

    @app.route("/health")
    def _health():
        return "ok", 200

    @app.cli.command("init-db")
    def init_db():
        """Create database tables."""
        db.create_all()
        print("Initialized the database.")

    return app
