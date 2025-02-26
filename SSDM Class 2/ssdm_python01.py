import pandas as pd 
import sqlite3 #connect to database

conn = sqlite3.connect('02_03_SSDM_Assignment_2_Zenara_subscription.db')
c = conn.cursor()

c.execute("SELECT name from sqlite_master WHERE type = 'table';")
c.fetchall()

df_sub = pd.read_sql_query("SELECT * FROM Subscriptions", conn)
