import flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test_lots.db'
db = SQLAlchemy(app)

Lot(db.Model):
    lot_id = db.Column(db.Integer, primary_key=True)
    corners = db.Column(db.String, unique=False, nullable=False)
    lot_type = db.Column(db.String(20), unique=False, nullable=False)
    num_spots = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return 'ID: %r' % lot_id

@app.route('/data/parkinglot', methods=['GET'])
def parkingData():
    return jsonify(test_data)

app.run()
