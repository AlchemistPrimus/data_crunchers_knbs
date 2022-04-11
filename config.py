
import os

#Getting the absolute path of the directory that the file resides in
basedir=os.path.abspath(os.path.dirname(__file__))
#Enabling the loading of the environment variables
from dotenv import load_dotenv
load_dotenv()


#Configuration classes

class Config:
    """Default configuration class. This config mode is to be applied by all the application modes(development,testing or deployment). Specific configuration modes will be overridden."""
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'data_kr_heroes'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    @staticmethod
    def init_app(app):
        """To enable application customize its configurations.
        Takes application instance as its parameter."""
        pass
    
class DevelopmentConfig(Config):
    """Development configuration class. contains necessary configuration for development specific configurations that should not be used in development"""
    DEBUG=True#This reloads the application everytime a change has been made, by restarting the server.
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'dev-data.sqlite')
    
class TestingConfig(Config):
    """Testing configuration class. contains test specific configuration for testing the application."""
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URL') or 'sqlite://'
    
class ProductionConfig(Config):
    """Production configuration class. This is the configuration that should be used for deployment or in the application during production."""
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'data.sqlite')
    
"""Dictionary for configuration options"""
config={
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DevelopmentConfig
}