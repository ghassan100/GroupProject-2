import os
import sqlite3
import pandas as pd

data_url = 'fm.csv'
headers = ['fmid','market_name','street','city','county','state','zip','website','facebook','twitter','youtube','othermedia','season1date','season1time','season2date','season2time','season3date','season3time','season4date','season4time','longitude','latitude','location','has_organic','has_bakedgoods','has_cheese','has_crafts','has_flowers','has_eggs','has_seafood','has_herbs','has_vegetables','has_honey','has_jams','has_maple','has_meat','has_nursery','has_nuts','has_plants','has_poultry','has_prepared','has_soap','has_trees','has_wine','has_coffee','has_beans','has_fruits','has_grains','has_juices','has_mushrooms','has_petfood','has_tofu','has_wildharvested','accepts_credit','accepts_wic','accepts_wiccash','accepts_sfmnp','accepts_snap','updatetime','updatetime_unparsed']
data_table = pd.read_csv(data_url, header=None, names=headers, converters={'zip': str})

# Clear example.db if it exists
if os.path.exists('example.db'):
    os.remove('example.db')

# Create a database
conn = sqlite3.connect('example.db')

# Add the data to our database

#data_table.to_sql('fmFeedback', conn, dtype={
#    'fmid': 'TEXT',
#    'market_name':'VARCHAR(256)',
#})


data_table.to_sql('fmMetadata', conn, dtype={
    'fmid': 'TEXT',
    'market_name' :'VARCHAR(256)',
    'street' :'VARCHAR(256)',
    'city' :'VARCHAR(256)',
    'county':'VARCHAR(256)',
    'state':'VARCHAR(256)',
    'zip':'VARCHAR(8)',
    'website':'VARCHAR(256)',
    'facebook':'VARCHAR(256)',
    'twitter':'VARCHAR(256)',
    'youtube':'VARCHAR(256)',
    'othermedia':'VARCHAR(256)',
    'season1date': 'datetime', 
    'season1time': 'datetime',
    'season2date': 'datetime',
    'season2time': 'datetime',
    'season3date': 'datetime',
    'season3timer': 'datetime',
    'season4dater': 'datetime',
    'season4time': 'datetime',
    'longitude':'VARCHAR(256)',
    'latitude':'VARCHAR(256)',
    'location': 'VARCHAR(256)',
    'has_organic': 'BOOLEAN',
    'has_bakedgoods': 'BOOLEAN',
    'has_cheese': 'BOOLEAN',
    'has_crafts': 'BOOLEAN',
    'has_flowers':'BOOLEAN', 
    'has_eggs': 'BOOLEAN',
    'has_seafood': 'BOOLEAN',
    'has_herbs': 'BOOLEAN',
    'has_vegetables': 'BOOLEAN',
    'has_honey':'BOOLEAN', 
    'has_jams':'BOOLEAN', 
    'has_maple':'BOOLEAN', 
    'has_meat':'BOOLEAN', 
    'has_nursery':'BOOLEAN', 
    'has_nuts':'BOOLEAN', 
    'has_plants':'BOOLEAN', 
    'has_poultry':'BOOLEAN', 
    'has_prepared':'BOOLEAN', 
    'has_soap':'BOOLEAN', 
    'has_trees':'BOOLEAN', 
    'has_wine':'BOOLEAN', 
    'has_coffee':'BOOLEAN', 
    'has_beans':'BOOLEAN', 
    'has_fruits':'BOOLEAN', 
    'has_grains':'BOOLEAN', 
    'has_juices':'BOOLEAN', 
    'has_mushrooms':'BOOLEAN', 
    'has_petfood':'BOOLEAN', 
    'has_tofu':'BOOLEAN', 
    'has_wildharvested':'BOOLEAN', 
    'accepts_credit':'BOOLEAN', 
    'accepts_wic':'BOOLEAN', 
    'accepts_wiccash':'BOOLEAN', 
    'accepts_sfmnp':'BOOLEAN', 
    'accepts_snap':'BOOLEAN', 
    'updatetime': 'datetime',
    'updatetime_unparsed' : 'datetime',
})
conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows
