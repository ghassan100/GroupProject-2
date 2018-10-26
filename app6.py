import unittest

from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import contains_eager, joinedload
from sqlalchemy.orm import relationship

#Create and engine and get the metadata
Base = declarative_base()
#engine = create_engine('ql://user:pass@Northwind', echo=True)
engine = create_engine('sqlite:///db/example.db',echo=True)
metadata = MetaData(bind=engine)
Base.metadata.reflect(engine)


#Reflect each database table we need to use, using metadata
class Fm_Metadata(Base):
    __table__ = Table('fmMetadata', metadata, autoload=True)
#    orders = relationship("Order", backref="customer")



class Test(unittest.TestCase):

    def setUp(self):
        #Create a session to use the tables    
        self.session = create_session(bind=engine)        

    def tearDown(self):
        self.session.close()

    def test_withJoins(self):
        q = self.session.query(Customer)
        q = q.join(Order)
        q = q.join(Shipper)
        q = q.filter(Customer.CustomerID =='ALFKI')
        q = q.filter(Order.OrderID=='10643')
        q = q.filter(Shipper.ShipperID=='1')
        q = q.options(contains_eager(Customer.orders, Order.shipper))
        res = q.all()
        cus = res[0]
        ord = cus.orders[0]
        shi = ord.shipper
        self.assertEqual(shi.Phone, '(503) 555-9831')
