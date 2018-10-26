from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Fm_Metadata,Fm_feedback
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)

engine = create_engine('sqlite:///db/example.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = automap_base()
@app.route("/")
def index(Base):
    return "hello world"

if __name__ == "__main__":
    app.run()
