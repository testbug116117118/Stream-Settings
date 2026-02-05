from flask import Flask
from flask_login import LoginManager
from config import Config
from models.user import User
from database import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
from routes.auth import auth_bp
from routes.streaming import streaming_bp
from routes.preferences import preferences_bp

app.register_blueprint(auth_bp)
app.register_blueprint(streaming_bp)
app.register_blueprint(preferences_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
