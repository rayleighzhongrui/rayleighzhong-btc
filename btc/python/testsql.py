import mysql.connector

conn = mysql.connector.connect(user='root', password='W6ya6dex5ngf4', database='btc', use_unicode=True)
cursor = conn.cursor()
sql_createtab = """create table btc_future_thisweek(
                  date VARCHAR (16) PRIMARY KEY ,
                  high FLOAT ,
                  vol FLOAT,
                  day_high FLOAT ,
                  last FLOAT ,
                  low FLOAT ,
                  contract_id BIGINT,
                  buy FLOAT ,
                  sell FLOAT ,
                  coin_vol FLOAT ,
                  day_low FLOAT ,
                  unit_amount FLOAT
                  )"""

cursor.execute(sql_createtab)
cursor.close()
