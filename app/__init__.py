import sys
sys.path.insert(0,'/home/ado/Desktop/new_datacranchers/data_crunchers_knbs/')
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config

"""Extensions used"""
bootstrap=Bootstrap()
moment=Moment()

def create_app(config_name):
    """Application factory function. This function is responsible for starting the instance of the application, and necessary initializations required by the application."""
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    #initializing extensions
    bootstrap.init_app(app)
    moment.init_app(app)
    
    
    from app.main.views import views
    app.register_blueprint(views)
    
    
    return app