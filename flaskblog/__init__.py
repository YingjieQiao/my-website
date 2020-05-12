from flask import Flask                 # importing the `Flask` class
from flask_sqlalchemy import SQLAlchemy # import SQL database extension
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


db = SQLAlchemy()                    # create the database (as class called "Model")
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
# pass in the function name of the route, same as passing function name into url_for()
login_manager.login_message_category = "info"
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)  # create the `Flask` class
    app.config.from_object(Config)

    db.init_app(app)  # create the database (as class called "Model")
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()

    return app