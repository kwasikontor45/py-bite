import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-key")
    # Flask's default static-file cache (4h) meant the last circadian.js fix
    # sat invisible in visitors' browsers for hours after deploy. Short
    # cache instead of none — still avoids re-fetching on every request.
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 60

    from . import routes

    app.register_blueprint(routes.bp)

    return app
