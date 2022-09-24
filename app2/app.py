import pandas as pd
import sqlalchemy
import mysql.connector

df = pd.read_csv('gs://covid-gcp-bucket1/data', sep=';', storage_options={'token': './sns-covid-gcp-b6475c6924f9.json'})
#print(df.head())

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root@34.141.87.84/covid')
print(engine.connect)
df.to_sql(name='table1', con=engine, if_exists = 'replace', index=False)