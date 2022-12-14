
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from .resources_storage import ResourcesStorage
from flask_migrate import Migrate
from sqlalchemy import MetaData



# init SQLAlchemy so we can use it later in our models
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)


db = SQLAlchemy(metadata=metadata)
migrate = Migrate()

resources = ResourcesStorage()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hsdhdhfgy36wg6dg'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    db.init_app(app)
    migrate.init_app(app, db=db, render_as_batch=True)
    

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    app.register_blueprint(resources.blueprint)
    

    return app
