"""Initialize Flask app."""
from flask import Flask

def create_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        from .dash_page import create_dashboard
        app = create_dashboard(app)

        # Import Dash application
        from .dashboard1.dashboard import create_dashboard
        app = create_dashboard(app)

        # Import second Dash application
        # from .plotlydash2.dashboard import create_dashboard
        # app = create_dashboard(app)

        return app
