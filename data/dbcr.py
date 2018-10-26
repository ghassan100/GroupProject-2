import sqlite3, csv
from sqlalchemy import create_engine
engine = create_engine('sqlite:///myfm.db', echo=False)
import pandas as pd
df = pd.read_csv('fm1.csv')
df.to_sql('fmMetadata', engine, if_exists='append', index=False)
