from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flasgger import Swagger
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
Swagger(app)
 
from my_app.gas_station.views import gas_station
app.register_blueprint(gas_station)

db.create_all()
