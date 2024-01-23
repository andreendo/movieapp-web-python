from flask import Flask
from flask_login import LoginManager
from app.model.user_dao import UserDao
# from config import SECRET_KEY


def create_app():
  app = Flask(__name__)
  login_manager = LoginManager()
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(user_id):
    userDAO = UserDao()
    return userDAO.find(user_id)
    
  # Load configuration from instance/config.py
  app.config.from_pyfile('instance/config.py', silent=False)
  app.secret_key = app.config['SECRET_KEY']
  # Import routes
  from . import routes
  app.register_blueprint(routes.bp)

  return app
