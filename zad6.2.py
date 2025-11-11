import csv
from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, Integer
from sqlalchemy import insert

engine = create_engine('sqlite:///zad6.db', echo=True)
conn= engine.connect()
meta = MetaData()


measure = Table(
'measure',meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('data', Float),
    Column('precip',Float),
    Column('tobs',Float),
)
station = Table(
    'station',meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
)

meta.create_all(engine)

def load_cvs(filename,table):
    with open(filename,newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
        conn.execute(insert(table), data)


load_cvs('clean_measure.csv',measure)
load_cvs('clean_stations.csv',station)


rows = conn.execute("select * from station LIMIT 5").fetchall()
for row in rows:
    print(row)

conn.close()