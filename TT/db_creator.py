from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///myfm.db', echo=True)
Base = declarative_base()

class Fm_Metadata(Base):
    """"""
    __tablename__ = "fmMetadata"

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
    season1date  = Column(Date)
    season1time  = Column(Date)
    season2date  = Column(Date)
    season2time  = Column(Date)
    season3date  = Column(Date)
    season3time  = Column(Date)
    season4date  = Column(Date)
    season4time  = Column(Date)
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
    updatetime = Column(Date) 
    updatetime_unparsed = Column(Date)

    def __init__(self,fmid,market_name,street,city,county,state,zip,website,facebook,twitter,youtube,othermedia,season1date,season1time,season2date,season2time,season3date,season3time,season4date,season4time,longitude,latitude,location,has_organic,has_bakedgoods,has_cheese,has_crafts,has_flowers,has_eggs,has_seafood,has_herbs,has_vegetables,has_honey,has_jams,has_maple,has_meat,has_nursery,has_nuts,has_plants,has_poultry,has_prepared,has_soap,has_trees,has_wine,has_coffee,has_beans,has_fruits,has_grains,has_juices,has_mushrooms,has_petfood,has_tofu,has_wildharvested,accepts_credit,accepts_wic,accepts_wiccash,accepts_sfmnp,accepts_snap,updatetime,updatetime_unparsed):
        """"""

        self.fmid=fmid
        self.market_name=market_name
        self.street=street
        self.city=city
        self.county=county
        self.state=state
        self.zip=zip
        self.website=website
        self.facebook=facebook
        self.twitter=twitter
        self.youtube=youtube
        self.othermedia=othermedia
        self.season1date=season1date
        self.season1time=season1time
        self.season2date=season2date
        self.season2time=season2time
        self.season3date=season3date
        self.season3time=season3time
        self.season4date=season4date
        self.season4time=season4time
        self.longitude=longitude
        self.latitude=latitude
        self.location=location
        self.has_organic=has_organic
        self.has_bakedgoods=has_bakedgoods
        self.has_cheese=has_cheese
        self.has_crafts=has_crafts
        self.has_flowers=has_flowers
        self.has_eggs=has_eggs
        self.has_seafood=has_seafood
        self.has_herbs=has_herbs
        self.has_vegetables=has_vegetables
        self.has_honey=has_honey
        self.has_jams=has_jams
        self.has_maple=has_maple
        self.has_meat=has_meat
        self.has_nursery=has_nursery
        self.has_nuts=has_nuts
        self.has_plants=has_plants
        self.has_poultry=has_poultry
        self.has_prepared=has_prepared
        self.has_soap=has_soap
        self.has_trees=has_trees
        self.has_wine=has_wine
        self.has_coffee=has_coffee
        self.has_beans=has_beans
        self.has_fruits=has_fruits
        self.has_grains=has_grains
        self.has_juices=has_juices
        self.has_mushrooms=has_mushrooms
        self.has_petfood=has_petfood
        self.has_tofu=has_tofu
        self.has_wildharvested=has_wildharvested
        self.accepts_credit=accepts_credit
        self.accepts_wic=accepts_wic
        self.accepts_wiccash=accepts_wiccash
        self.accepts_sfmnp=accepts_sfmnp
        self.accepts_snap=accepts_snap
        self.updatetime=updatetime
        self.updatetime_unparsed=updatetime_unparsed
# create tables
Base.metadata.create_all(engine)
