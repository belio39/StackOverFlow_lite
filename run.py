"""This is a module"""
import os

from app.views import create_app
from database import database

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)

database(app)

if __name__ == '__main__':
    app.run(debug=True)
