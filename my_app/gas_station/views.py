import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from flasgger import swag_from

from my_app import db, app
from my_app.gas_station.models import GasStation
from my_app.gas_station.api_doc import get, post


 
gas_station = Blueprint('gas_station', __name__)
 
@gas_station.route('/')
@gas_station.route('/home')
def home():
    return "Welcome to the Gas Station Home."
 
 
class GasStationView(MethodView):
    @swag_from(get)
    def get(self, id=None, page=1):
        """
            API Gas Station.
            Call this api passing a id gas_station and get back its features,
            or not passing id and return all gas_stations.
            ---
            tags:
              - Gas Station API

        """
        if not id:
            gas_stations = GasStation.query.paginate(page, 10).items
            res = {}
            for gas_station in gas_stations:
                res[gas_station.id] = {
                    "place_id": str(gas_station.place_id),
                    "name": gas_station.name,
                    "latitude": str(gas_station.latitude),
                    "longitude": str(gas_station.longitude),
                    "rating": str(gas_station.rating),
                    "vicinity": str(gas_station.vicinity)
                }
        else:
            gas_station = GasStation.query.filter_by(id=id).first()
            if not gas_station:
                abort(404)
            res = {
                "place_id": str(gas_station.place_id),
                "name": gas_station.name,
                "latitude": str(gas_station.latitude),
                "longitude": str(gas_station.longitude),
                "rating": str(gas_station.rating),
                "vicinity": str(gas_station.vicinity)
            }
        return jsonify(res)

    @swag_from(post)
    def post(self):
        """
            API Gas Station.
            Call this api passing parameters to create a gas station object.
            ---
            tags:
              - Gas Station API
        """
        place_id = request.form.get('place_id')
        name = request.form.get('name')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        rating = request.form.get('rating')
        vicinity = request.form.get('vicinity')
        gas_station = GasStation(
            place_id, name, latitude, longitude, rating, vicinity
        )

        db.session.add(gas_station)
        db.session.commit()

        return jsonify({gas_station.id: {
            'name': gas_station.name,
            'place_id': gas_station.place_id,
            'vicinity': gas_station.vicinity
        }})

    def put(self, id):
        gas_station = GasStation.query.filter_by(id=id).first()
        # for req in request.form:
        #     if req in GasStation.__dict__.keys():
        #         gas_station[req] = request.form.get(req)
        return ''
    def delete(self, id):
        # Delete the record for the provided id.
        return
 
 
gas_station_view = GasStationView.as_view('gas_station_view')
app.add_url_rule(
    '/gas_station/', view_func=gas_station_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/gas_station/<int:id>', view_func=gas_station_view, methods=['GET', 'PUT']
)