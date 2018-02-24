from apscheduler.schedulers.blocking import BlockingScheduler
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import ssl
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
# set the config
apikey = 'XXX'
secretkey = 'XXX'
okcoinRESTURL = 'www.okex.com'
column = ['date', 'high', 'vol', 'day_high', 'last', 'low', 'contract_id', 'buy', 'sell', 'coin_vol', 'day_low', 'unit_amount']

# create tempdata
# tempdata = pd.DataFrame(columns=column)
conn = mysql.connector.connect(user='root', password='W6ya6dex5ngf4', database='btc', use_unicode=True)
yconnect = create_engine('mysql://root:W6ya6dex5ngf4@localhost:3306/btc?charset=utf8')
print('database has connected')
#set ssl config 总是报SSL错误，没办法只能加上下面这句，不验证SSL了。
ssl._create_default_https_context = ssl._create_unverified_context
#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL, apikey, secretkey)
#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL, apikey, secretkey)
print('start to request')
def job():
    zr_mk_qian = okcoinFuture.future_ticker('btc_usd', 'this_week')
#    print(zr_mk_qian)
    tempdata = pd.DataFrame([[zr_mk_qian['date']] + list(zr_mk_qian['ticker'].values())], columns=column)
    cursor = conn.cursor()
#    tempdata = [zr_mk_qian['date']] + list(zr_mk_qian['ticker'].values())
#    print(len(tempdata))
#    cursor.execute("insert into btc_future_thisweek VALUES ([zr_mk_qian['date']] + list(zr_mk_qian['ticker'].values()))")
    pd.io.sql.to_sql(tempdata, 'btc_future_thisweek', yconnect, schema='btc', index = False, if_exists='append')
    print('the data has saved')
#    conn.commit()
#    cursor.close()


#    print(tempdata)

job_defaults = {
    'coalesce': False,
    'max_instances': 5
}
# 定义BlockingScheduler
sched = BlockingScheduler(job_defaults = job_defaults)
sched.add_job(job, 'interval', seconds=5)

sched.start()
