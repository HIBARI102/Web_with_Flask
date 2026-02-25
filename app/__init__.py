import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Package-level DB instance (initialized in create_app)
db = SQLAlchemy()


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

    # Import models so they are registered with SQLAlchemy
    with app.app_context():
        try:
            from . import models  # noqa: F401
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

    @app.route("/health")
    def _health():
        return "ok", 200

    @app.cli.command("init-db")
    def init_db():
        """Create database tables."""
        db.create_all()
        print("Initialized the database.")

    return app
