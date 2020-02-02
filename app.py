# PROJ: Everett Parking
# AUTH: Krish Kalai, Jun Zhen, Jermey Tandjung
# DATE: Feb 02, 2021

from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/lots231.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Lot(db.Model):
    """
    The model for the database.
    
    lot_id: The primary key for the database, It is an unique integer.
    corners: The coordinates of the polygon. The format is latitude and longitude separated by a comma. Superseding pairs are comma separated. There is no comma at the end.
    lot_type: The type of the lot, as specified in the downtown parking map document. all characters are lowercase.
    num_spots: The number of available spots in the lot or street parking row.
    
    To be added:
    restrictions: A number representing independent restructions modes. Each bit symbolizies an unique restruction.
        Bit 0 (LSB): does a time restriction exist
        Bit 1: permit required
        Bit 2: handicap
        Bit 3: bus zone
        Bit 4: loading zone
        Bit 5: senior citizen permit
        Bit 6: official vehicle only
        Bit 7: high school permit only
    time_restriction: An integer representing the time restriction. If Bit 0 of restrictions is clear, then this is 0.
    """
    lot_id = db.Column(db.Integer, primary_key=True)
    corners = db.Column(db.String, unique=False, nullable=False)
    lot_type = db.Column(db.Integer, unique=False, nullable=False)
    num_spots = db.Column(db.Integer, unique=False, nullable=False)
    restriction = db.Column(db.Integer, unique=False, nullable=False)
    time_restriction = db.Column(db.String, unique=False, nullable=False)
    

    def __repr__(self):
        return 'ID: %r' % self.lot_id

@app.route('/data/parkinglot', methods=['GET'])
def parkingData():
    """
    Request to get all the lots' data from the database. The response format is as follows
    [
        "coords" : [
            {
                "latitude" : (float)
                "longitude" : (float)
            }
        ]
        "id" : (int)
        "num_spots" : (int)
        "type" : (string) (future: simplify to int)
    ]

    """
    lots = Lot.query.all()
    locations = []
    for lot in lots:
        location = {}
        location['id'] = lot.lot_id
        location['type'] = lot.lot_type
        location['num_spots'] = lot.num_spots
        location['restriction'] = lot.restriction
        location['time_restriction'] = lot.time_restriction

        pairs = []
        _pairs = lot.corners.split(",")
        for i in range(0,len(_pairs),2):
            pair = {}
            pair["latitude"] = float(_pairs[i])
            pair["longitude"] = float(_pairs[i+1])
            pairs.append(pair)
        location['coords'] = pairs
        locations.append(location)
    return jsonify(locations)

@app.route('/data/add', methods=['GET'])
def addLot():
    """
    Create a record with the data passed in.

    Future work:
    Validate input data
    Use environment variable/authentication to disable/restrict calls to this function
    """

    #Get all data from query params
    lot_id = request.args.get('id')
    lot_type = request.args.get('type')
    coords = request.args.get('coords')
    num_spots = request.args.get('num_spots')
    restriction = request.args.get('restriction')
    time_restriction = request.args.get('time_restriction')

    coord_validate_code = validate_coordinates(coords)
    if coord_validate_code != 0:
        # Coordinates are invalid
        fail_reason = {
            1: "Number of elements not even",
            2: "Latitude out of range",
            3: "Longitude out of range"
        }[coord_validate_code]
        abort(400, description="Reason: " + fail_reason)

    new_lot = Lot(lot_id=lot_id,
                  corners=coords,
                  lot_type=lot_type,
                  num_spots=num_spots,
                  restriction=restriction,
                  time_restriction=time_restriction)
    db.session.add(new_lot)
    try:
        db.session.commit()
    except:
        print("ERROR: Adding to the database failed, possibly due to mismatching keys")
        abort(400, description="Reason: Commit failed")

    return str(new_lot)

def validate_coordinates(string):
    """
    Returns true if the input string is valid. The criteia is as follows
    1) There must be an even number of elements
    2) Every even element must be a latitude
    3) Every odd element must be a longitude
    """

    coordinates = string.split(",")
    if len(coordinates) % 2 == 1:
        print("ERROR: number of elements not even")
        return 1

    for i in range(0,len(coordinates)):
        value = float(coordinates[i])
        if i % 2 == 0 and (value < -90 or value > 90):
            print("ERROR: latitude out of range (element ", i, )
            return 2
        if i % 2 == 1 and (value < -180 or value > 80):
            print("ERROR: longtitude out of range")
            return 3

    return 0

# Create the database (if not exist) upon server begin and start listening
db.create_all()
app.run(host="0.0.0.0")
