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
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"Stations: /api/v1.0/stations<br/>"
        f"TOBS: /api/v1.0/tobs<br/>"
        f"Start Date: /api/v1.0/start<br/>"
        f"Start/End Date: /api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    #recent_year = dt.date(2017, 8, 23)
    #year_before = recent_year - dt.timedelta(days=365)
    precipitation = session.query(measurement.date, measurement.prcp).filter(measurement.date >= '2016-08-24').all()
    total_prcp = []
    for date,prcp  in precipitation:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
               
        total_prcp.append(prcp_dict)

    return jsonify(total_prcp)


@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(station.station).order_by(station.station).all()
    station_list = list(np.ravel(stations))
    return jsonify(station_list=station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    temps = session.query(measurement.date, measurement.tobs, measurement.prcp).\
                filter(measurement.date >= '2016-08-23').\
                filter(measurement.station=='USC00519281').\
                order_by(measurement.date).all()
    
    total_tobs = []
    for prcp, date,tobs in temps:
        tobs_dict = {}
        tobs_dict["prcp"] = prcp
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        
        total_tobs.append(tobs_dict)
    return jsonify(total_tobs)


@app.route("/api/v1.0/<start>")
def start_date(start):
    start_date = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= '2016-08-23').all()
    session.close()

    start_tobs = []
    for min,avg,max in start_date:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        start_tobs.append(tobs_dict)

    return jsonify(start_tobs)


@app.route("/api/v1.0/<start>/<end>")
def end_date(start, end):

    end_date = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
                filter(measurement.date >= '2016-08-23').filter(measurement.date <= '2017-08-23').all()

    
  
    # Create a dictionary from the row data and append to a list of start_end_date_tobs
    end_tobs = []
    for min, avg, max in end_date:
        end_tobs_dict = {}
        end_tobs_dict["min_temp"] = min
        end_tobs_dict["avg_temp"] = avg
        end_tobs_dict["max_temp"] = max
        end_tobs.append(end_tobs_dict) 
    

    return jsonify(end_tobs)


if __name__=="__main__":
        app.run(debug=True)
    
