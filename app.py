import flask
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/lots231.db'
db = SQLAlchemy(app)

class Lot(db.Model):
    lot_id = db.Column(db.Integer, primary_key=True)
    polygon_id = db.Column(db.String, unique=True, nullable=False)
    corners = db.Column(db.String, unique=False, nullable=False)
    lot_type = db.Column(db.String, unique=False, nullable=False)
    num_spots = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return 'ID: %r' % self.lot_id

test_data =  { 
    "locations": [{
        "coords": [{
            "latitude": 47.980802, 
            "longitude": -122.213511
        }, {
            "latitude": 47.980802, 
            "longitude": -122.213037
        }, {
            "latitude": 47.981574, 
            "longitude": -122.213015
        }, {
            "latitude": 47.981571, 
            "longitude": -122.213274
        }, {
            "latitude": 47.981887, 
            "longitude": -122.213275
        }, {
            "latitude": 47.981888, 
            "longitude": -122.213497
        }], 
        "type": "Public Lot",
        "num_spots": 97,
        "id": 1,
        "polygon_id": "California Ave & Grand Ave"
    }, {
        "coords": [{
            "latitude": 47.978065,
            "longtiude": -122.204532 
        }, {
            "latitude": 47.978053,
            "longtiude": -122.205017 
        }, {
            "latitude": 47.978724,
            "longtiude": -122.205061 
        }, {
            "latitude": 47.978733,
            "longtiude": -122.204572 
        }], 
        "type": "Private Lot",
        "num_spots": 83,
        "id": 2,
        "polygon_id": "Wall St. & Oakeys Ave"
    }, {
        "coords": [{
            "latitude": 47.989860,
            "longtiude": -122.209929 
        }, {
            "latitude": 47.980950,
            "longtiude": -122.209309 
        }, {
            "latitude": 47.981566,
            "longtiude": -122.209299
        }, {
            "latitude": 47.981572,
            "longtiude": -122.209795
        }], 
        "type": "Private Lot",
        "num_spots": 86,
        "id": 3,
        "polygon_id": "California Ave & Hoyt Ave"
    }, {
        "coords": [{
            "latitude": 47.976535,
            "longtiude": -122.210673
        }, {
            "latitude": 47.976501,
            "longtiude": -122.211352
        }, {
            "latitude": 47.977024,
            "longtiude": -122.210697
        }, {
            "latitude": 47.977014,
            "longtiude": -122.211355
        }], 
        "type": "Private Lot",
        "num_spots": 37,
        "id": 4,
        "polygon_id": "Pacific Ave & Rucker Ave"
    }, {
        "coords": [{
            "latitude": 47.981477,
            "longtiude": -122.206490
        }, {
            "latitude": 47.981484,
            "longtiude": -122.207167 
        }, {
            "latitude": 47.981008,
            "longtiude": -122.207172 
        }, {
            "latitude": 47.980988,
            "longtiude": -122.206514
        }], 
        "type": "Private Lot",
        "num_spots": 52,
        "id": 5,
        "polygon_id": "California Ave & Wetmore Ave"
    }]
}

@app.route('/data/parkinglot', methods=['GET'])
def parkingData():
    print(Lot.query.filter())
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
    db.session.commit()
    return str(new_lot)

db.create_all()
app.run(host="0.0.0.0")
