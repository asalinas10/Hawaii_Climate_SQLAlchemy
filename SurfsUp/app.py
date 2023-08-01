# Import the dependencies.

# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
import datetime as dt
import numpy as np


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

# reflect an existing database into a new model

Base = automap_base()

# reflect the tables


Base.prepare(autoload_with=engine)


# Save references to each table

measurement = Base.classes.measurement
station = Base.classes.station


# Create our session (link) from Python to the DB

session = Session(engine)

#################################################
# Flask Setup
#################################################

from flask import Flask, jsonify

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    recent_year = dt.date(2017, 8, 23)
    year_before = recent_year - dt.timedelta(days=365)
    precipitation = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year_before).all()
    last_rain = {date: prcp for date, prcp in precipitation}
    return jsonify(last_rain)

@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(station.station).all()
    station_list = list(np.ravel(stations))
    return jsonify(station_list=station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    year_before = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temps = session.query(measurement.tobs).\
    filter(measurement.station == 'USC00519281').\
    filter(measurement.date >= year_before).all()
    temps_list = list(np.ravel(temps))
    return jsonify(temps_list=temps_list)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")

def temps(start=None, end=None):
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
    if not end:
                results = session.query(*sel).\
                        filter(measurement.date >= start).\
                        filter(measurement.date <= end).all()
                data = list(np.ravel(results))
                return jsonify(data)
    results = session.query(*sel).\
                        filter(measurement.date >= start).\
                        filter(measurement.date <= end).all()
    data = list(np.ravel(results))
    return jsonify(data)

if __name__=="__main__":
        app.run(debug=True)
    
