import flask
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from lot import db,Lot

app = flask.Flask(__name__)
app.config['DEBUG'] = True

test_data = { 
    "locations": [{
        "coords": [{
            "longitude": 47.980802, 
            "latitude": -122.213511
        }, {
            "longitude": 47.980802, 
            "latitude": -122.213037
        }, {
            "longitude": 47.981574, 
            "latitude": -122.213015
        }, {
            "longitude": 47.981571, 
            "latitude": -122.213274
        }, {
            "longitude": 47.981887, 
            "latitude": -122.213275
        }, {
            "longitude": 47.981888, 
            "latitude": -122.213497
        }], 
        "type": "Public Lot",
        "num_spots": 97,
        "id": 1,
        "polygon_id": "California Ave & Grand Ave"
    }, {
        "coords": [{
            "longitude": 47.978065,
            "latitude": -122.204532 
        }, {
            "longitude": 47.978053,
            "latitude": -122.205017 
        }, {
            "longitude": 47.978724,
            "latitude": -122.205061 
        }, {
            "longitude": 47.978733,
            "latitude": -122.204572 
        }], 
        "type": "Private Lot",
        "num_spots": 83,
        "id": 2,
        "polygon_id": "Wall St. & Oakeys Ave"
    }]
}

@app.route('/data/parkinglot', methods=['GET'])
def parkingData():
    #Lot.query.all()
    return jsonify(test_data)

@app.route('/data/add', methods=['GET'])
def addLot():
    lot_id = request.args.get('id')
    polygon_id = request.args.get('polygon_id')
    lot_type = request.args.get('type')
    coords = request.args.get('coords')
    num_spots = request.args.get('num_spots')

    new_lot = Lot(lot_id=lot_id,
                         polygon_id=polygon_id,
                         corners=coords,
                         lot_type=lot_type,
                         num_spots=num_spots)
    db.session.add(new_lot)

app.run(host="0.0.0.0")
