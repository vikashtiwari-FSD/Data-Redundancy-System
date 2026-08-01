from flask import Flask

from routes.home import home_bp
from routes.dashboard import dashboard_bp

app = Flask(__name__)

app.secret_key = "codealpha123"

app.register_blueprint(home_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)