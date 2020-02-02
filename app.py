import flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['DEBUG'] = True

test_data = {
	"locations": [{
		"coords": [{
			"longitude": 10,
			"latitude": 10
		}, {
			"longitude": 10,
			"latitude": 20
		}, {
			"longitude": 20,
			"latitude": 10
		}, {
			"longitude": 20,
			"latitude": 20
		}],
		"type": "Public Lot",
		"numSpots": 5
	}, {
		"coords": [{
			"longitude": 100,
			"latitude": 100
		}, {
			"longitude": 100,
			"latitude": 200
		}, {
			"longitude": 200,
			"latitude": 100
		}, {
			"longitude": 200,
			"latitude": 200
		}],
		"type": "Private Lot",
		"numSpots": 200
	}]
}

@app.route('/data/parkinglot', methods=['GET'])
def parkingData():
    return jsonify(test_data)

app.run(host="0.0.0.0")
