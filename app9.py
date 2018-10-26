import os
import sqlite3
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template,abort
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, desc
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.sql import label
app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
conn = db.engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Link = Base.classes.link

'''
@app.route("/")
def index():
    return render_template("index.html")
'''
@app.route("/Items")
def Items():
    """Return a list of items names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Link).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column Items (Item  names)
    print(jsonify(list(df.columns)[:]))
    return jsonify(list(df.columns)[4:])

'''
@app.route("/popular")
def popular():
    from sqlalchemy import select
    """Return a list of items names."""
    # Use Pandas to perform the sql query
    stmt = db.session.query(Link).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    from sqlalchemy import func
    foo= db.session.query(Link.Item,func.count(Link.Item)).group_by(Link.Item).all()

    print(list(foo))
    return jsonify(list(foo)) 
'''
"""
    s = select([Link])
    print(str(s))
    rs = conn.execute(s)
    for row in rs:
"""
'''
    print(r)
    aa=db.session.query(
    Expense.date,
    func.sum(Expense.value).label('total')
    ).join(Expense.cost_center
    ).filter(CostCenter.id.in_([2, 3])
    ).group_by(Expense.date
    ).all()
    print(r)
#   for s in df:
#       print (s.Date, s.Item)
#   # Return a list of the column Items (Item  names)
'''

@app.route("/metadata")
def link_metadata():
    """Return the MetaData for a given sample."""
    sel = [
        Link.id,
        Link.Date,
        Link.Time,
        Link.Transection,
        Link.Item
    ]

#    results = db.session.query(*sel).all()
    results = db.session.query(*sel).filter(Link.id == Link.id).all()

    print(results)
    # Create a dictionary entry for each row of metadata information
    link_metadata = {}
    for result in results:
        link_metadata["Transection"] = result[3]
        link_metadata["Item"] = result[4]

    print(link_metadata)
    return jsonify(link_metadata)

if __name__ == "__main__":
    app.run()
