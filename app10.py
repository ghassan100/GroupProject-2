###########################################
# imports dependencies
###########################################
from datetime import datetime as dt
from bokeh.io import output_file
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
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
@app.route("/doww")
def doww():
   #for Date, count in session.query(Info.Date,
   #   func.count(Info.Item)).group_by(Info.Date).all():
   #   print (Date, count)
    dd=session.query(func.count(Info.Item).label('qty'))\
       .group_by(Info.Date).order_by(desc('qty'))
    keys11 = [dd[x][0] for x in range(len(dd))]
    print(keys11)
    error="none"
    return  error
#   return render_template('in5.html',data=data)

@app.route("/popular")
def pop():
    foo = session.query(func.count(Info.Transection),Info.Item).\
    group_by(Info.Item).order_by(Info.Item).all()
    data2= json.dumps([{"date": foo[x][1],"value": foo[x][0]}
        for x in range(len(foo))],default=to_serializable)
    data={'chart_data':data2}
    print(data)
#   return render_template('vega.html',data=data)
    return render_template('in8.html',data=data)

@app.route("/Items")
def items():
    """Return Dates and Temp from the last year."""
    results = session.query(Info.Date, Info.id).\
        filter(Info.Date >= "2016-10-30", Info.Date <= "2017-01-23").\
        all()
# creates JSONified list
    info_list = [results]

    print( jsonify(info_list))
    return jsonify(info_list)
from datetime import datetime
from functools import singledispatch

@singledispatch
def to_serializable(val):
    """Used by default."""
    return str(val)
    
@to_serializable.register(datetime)
def ts_datetime(val):
    """Used if *val* is an instance of datetime."""
    return val.isoformat() + "Z"
def dow(date):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dayNumber=date.weekday()
    print(days[dayNumber])

@app.route("/groupby")
def groupby():
    from sqlalchemy import func
    posts = session.query(Info).order_by(Info.Item)
    print(posts)
    foo = session.query(func.count(Info.Transection),Info.Item).\
    group_by(Info.Item).order_by(Info.Item).all()
    print(foo)
    foo2 = session.query(func.count(Info.Date),Info.Item).\
    group_by(Info.Item).order_by(Info.Item).all()
    #distinct_dates = list(session.query(func.DATE(Info.Date)).distinct())
    data1 = session.query(func.count(Info.Item),Info.Date).\
    group_by(Info.Date).order_by(Info.Date).all()
    values = [data1[x][0] for x in range(len(data1))]
    keys1 = [data1[x][1] for x in range(len(data1))]
    for keys1 in keys1: 
        print(time.strftime("%A", time.strptime(str(keys1), "%Y-%m-%d")))
    #print(jsonify(info_list))
#      for x in range(len(data1)) 
#    for x in range(len(data1)):
#   print(time.strftime("%A", time.strptime(str(Info.Date), "%Y-%m-%d")))
    #print(Info.Date)
    data2= json.dumps([{"Date": data1[x][1],"High": data1[x][0]}
        for x in range(len(data1))],default=to_serializable)
#   plot = figure()
    plot = figure(x_axis_type='datetime')
#    plot.vbar(x=x, bottom=0, top=y, width=0.1, color="blue")
    data={'chart_data':data2} 
    print(data)
    plot.line(keys1,values)
#    return Markup(file_html(plot, CDN, "my plot"))
    return render_template('index.html',data=data)



if __name__ == '__main__':
    app.run(debug=True)
