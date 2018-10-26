###########################################
# imports dependencies
###########################################
from datetime import datetime
from functools import singledispatch
from datetime import datetime as dt
from flask import Flask, Markup
import datetime
import time
import json
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func,desc
import collections
from flask import Flask, jsonify

###########################################
# initializes database
###########################################

engine = create_engine("sqlite:///database.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

###########################################
# creates references to Info
# and Station tables
###########################################

Info = Base.classes.link

session = Session(engine)

####################################
# initializes Flask app
####################################
app = Flask(__name__)

################################
# initializes Flask Routes
################################
"""
"""
#rendering the HTML page which has the button
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)
@app.route('/addRegion', methods=['POST'])
def handle_data():
    foo = session.query(func.count(Info.Transection),Info.Item).\
    group_by(Info.Item).order_by(Info.Item).all()
    data2= json.dumps([{"date": foo[x][1],"value": foo[x][0]}
        for x in range(len(foo))],default=to_serializable)
    data={'chart_data':data2}
    print(data)
    return (request.form['projectFilePath'])


@singledispatch
def to_serializable(val):
    """Used by default."""
    return str(val)
    
@to_serializable.register(datetime)
def ts_datetime(val):
    """Used if *val* is an instance of datetime."""
    return val.isoformat() + "Z"



if __name__ == '__main__':
    app.run()
