from my_app import db
 
class GasStation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    place_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    latitude = db.Column(db.Float(asdecimal=True))
    longitude = db.Column(db.Float(asdecimal=True))
    rating = db.Column(db.Float(asdecimal=True))
    vicinity = db.Column(db.String(255))

    def __init__(self, place_id, name, latitude, longitude, rating, vicinity):
        self.place_id = place_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.rating = rating
        self.vicinity = vicinity
 
    def __repr__(self):
        return '<Product %d>' % self.id