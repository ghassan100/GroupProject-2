# models.py 
 
from app8 import db
 
 
class Fm_Metadata(db.Model):
    __tablename__ = "fmMetadata"
 
    fmid = db.Column(db.Integer, primary_key=True)
    market_name = db.Column(db.String)
 
    def __repr__(self):
        return "<Fm_Metadata: {}>".format(self.name)
