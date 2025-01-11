from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register controllers
    from app.controllers import scraper_bp
    app.register_blueprint(scraper_bp)

    return app
