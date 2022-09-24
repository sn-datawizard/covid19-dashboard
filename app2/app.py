import pandas as pd
import sqlalchemy
import mysql.connector

df = pd.read_csv('gs://*', sep=';', storage_options={'token': './KEYFILE.json'}) #Sensitive data not visible
#print(df.head())

engine = sqlalchemy.create_engine('mysql+mysqlconnector://user:password@databaseip/covid') #Sensitive data not visible
print(engine.connect)
df.to_sql(name='table1', con=engine, if_exists = 'replace', index=False)
