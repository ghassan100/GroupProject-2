import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import Boolean, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Fm_feedback(Base):
    __tablename__ = 'fmFeedback'

    fmid = Column(Integer, primary_key=True)
    market_name = Column(String(30), nullable=False)


class Fm_Metadata(Base):
    __tablename__ = 'fmMetadata'

    fmid = Column(Integer, primary_key=True)
    market_name = Column(String(80), nullable=False)
    street = Column(String(250))
    city = Column(String(8))
    county = Column(String(8))
    state = Column(String(8))
    zip = Column(String(8))
    website = Column(String(250))
    facebook=Column(String(250))
    twitter=Column(String(250))
    youtube=Column(String(250))
    othermedia=Column(String(250))
    season1date  = Column(DateTime, default=datetime.datetime.utcnow)
    season1time  = Column(DateTime, default=datetime.datetime.utcnow)
    season2date  = Column(DateTime, default=datetime.datetime.utcnow)
    season2time  = Column(DateTime, default=datetime.datetime.utcnow)
    season3date  = Column(DateTime, default=datetime.datetime.utcnow)
    season3time  = Column(DateTime, default=datetime.datetime.utcnow)
    season4date  = Column(DateTime, default=datetime.datetime.utcnow)
    season4time  = Column(DateTime, default=datetime.datetime.utcnow)
    longitude =Column(String(8))
    latitude=Column(String(8))
    location=Column(String(250))
    has_organic = Column(Boolean)
    has_bakedgoods = Column(Boolean)
    has_cheese = Column(Boolean)
    has_crafts = Column(Boolean)
    has_flowers = Column(Boolean)
    has_eggs = Column(Boolean)
    has_seafood = Column(Boolean)
    has_herbs = Column(Boolean)
    has_vegetables = Column(Boolean)
    has_honey = Column(Boolean)
    has_jams = Column(Boolean)
    has_maple = Column(Boolean)
    has_meat = Column(Boolean)
    has_nursery = Column(Boolean)
    has_nuts = Column(Boolean)
    has_plants = Column(Boolean)
    has_poultry = Column(Boolean)
    has_prepared = Column(Boolean)
    has_soap = Column(Boolean)
    has_trees = Column(Boolean)
    has_wine = Column(Boolean)
    has_coffee = Column(Boolean)
    has_beans = Column(Boolean)
    has_fruits = Column(Boolean)
    has_grains = Column(Boolean)
    has_juices = Column(Boolean)
    has_mushrooms = Column(Boolean)
    has_petfood = Column(Boolean)
    has_tofu = Column(Boolean)
    has_wildharvested = Column(Boolean)
    accepts_credit = Column(Boolean)
    accepts_wic = Column(Boolean)
    accepts_wiccash = Column(Boolean)
    accepts_sfmnp = Column(Boolean)
    accepts_snap = Column(Boolean)
    updatetime = Column(DateTime, default=datetime.datetime.utcnow) 
    updatetime_unparsed = Column(DateTime, default=datetime.datetime.utcnow)
    fmFeedback = relationship(Fm_feedback)
engine = create_engine('sqlite:///db/farmers_markets.sqlite')


Base.metadata.create_all(engine)
