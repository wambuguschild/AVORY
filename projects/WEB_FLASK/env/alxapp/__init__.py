from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from os import path
import os





db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = 'lets go'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(DB_NAME)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    static_folder_path = os.path.join(os.path.dirname(__file__), 'static')
    app.config['STATIC_FOLDER'] = static_folder_path

    
    
    db.init_app(app)
    


    from .views import views
    from .fashion_page import fashion
    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(fashion, url_prefix='/fashion_recommendation')
    

    from .models import Profile
    
    create_database(app)

    
    return app

def create_database(app):
    with app.app_context():
        if not path.exists(f'alxapp/{DB_NAME}'):
            db.create_all()
            print('database have been created')


