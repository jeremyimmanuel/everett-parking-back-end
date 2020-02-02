import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/lots.db'
db = SQLAlchemy(app)

class Lot(db.Model):
    lot_id = db.Column(db.Integer, primary_key=True)
    polygon_id = db.Column(db.String, unique=True, nullable=False)
    corners = db.Column(db.String, unique=False, nullable=False)
    lot_type = db.Column(db.String, unique=False, nullable=False)
    num_spots = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return 'ID: %r' % self.lot_id
