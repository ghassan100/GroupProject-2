from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, relationship
from sqlalchemy import create_engine, Column, String

Base = automap_base()

engine = create_engine('sqlite:///db/example.db', echo=True)
Base = declarative_base()

# pre-declare User for the 'user' table
class User(Base):
    __tablename__ = 'user'

    # override schema elements like Columns
    oname = Column('originalname', String)

    # and a relationship. I name it 'weird' because in my database schema
    # this relationship makes absolutely no sense, but it does demonstrate
    # the point
    weird = relationship("usergroup",
                         foreign_keys='usergroup.id',
                         primaryjoin='and_(usergroup.id==User.id)')

Base.prepare(engine, reflect=True)
session = Session(engine)

# Test this by querying the User table and then following the relationship
u = session.query(User).filter(User.oname == 'testuser').one()
print (u.oname)
for g in u1.weird:
    print (g.name)
