from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import time
import ssl
import pandas as pd

apikey = 'XXX'
secretkey = 'XXX'
okcoinRESTURL = 'www.okex.com'
column = ['date', 'high', 'vol', 'day_high', 'last', 'low', 'contract_id', 'buy', 'sell', 'coin_vol', 'day_low',
          'unit_amount']
tempdata = pd.DataFrame(columns=column)
head = column
i = 0
# set ssl config 总是报SSL错误，没办法只能加上下面这句，不验证SSL了。
ssl._create_default_https_context = ssl._create_unverified_context
# 现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL, apikey, secretkey)
# 期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL, apikey, secretkey)


def job():
    zr_mk_qian = okcoinFuture.future_ticker('btc_usd', 'this_week')
    tempdata.loc[tempdata.shape[0]] = [zr_mk_qian['date']] + list(zr_mk_qian['ticker'].values())
    tempdata.loc[(tempdata.shape[0] - 1):(tempdata.shape[0])].to_csv('BTC_thisweek_future.csv', index=None, header=None,
                                                                     sep=',', mode='a+', encoding='utf-8')

    if tempdata.shape[0] > 840:
        return

    # print(tempdata)


job_defaults = {
    'coalesce': False,
    'max_instances': 5
}
# 定义BlockingScheduler
sched = BlockingScheduler(job_defaults=job_defaults)
sched.add_job(job, 'interval', seconds=1)

sched.start()
