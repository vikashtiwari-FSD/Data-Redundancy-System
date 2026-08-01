from flask import Flask

from routes.home import home_bp
from routes.dashboard import dashboard_bp
from routes.search import search_bp
from firebase.firebase_config import db

app = Flask(__name__)

app.secret_key = "codealpha123"

app.register_blueprint(home_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(search_bp)

if __name__ == "__main__":
    app.run(debug=True)