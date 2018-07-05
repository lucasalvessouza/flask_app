from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flasgger import Swagger
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

app.config['SWAGGER'] = {
    'uiversion': 3
}

template = {
  "swagger": "2.0",
  "info": {
    "title": "API 0",
    "description": "API for my data",
    "contact": {
      "responsibleOrganization": "ME",
      "responsibleDeveloper": "Me",
      "email": "lucasalves.souza01@gmail.com",
      "url": "",
    },
    "termsOfService": "http://me.com/terms",
    "version": "0.0.1"
  },
  "host": "localhost:5000",
  "basePath": "/api",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"
}

Swagger(app, template=template)
 
from my_app.gas_station.views import gas_station
app.register_blueprint(gas_station)

db.create_all()
