from flask import Flask



def create_app(config_name):
    """Application factory function. This function is responsible for starting the instance of the application, and necessary initializations required by the application."""
    app=Flask(__name__)
    return app