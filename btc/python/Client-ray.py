# -*- coding:utf-8 -*-
# encoding:utf-8
#新写的btc的脚本

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import time
import ssl
import pandas as pd

apikey = 'XXX'
secretkey = 'XXX'
okcoinRESTURL = 'www.okex.com'
#df_empty = pd.DataFrame(columns=['tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min', 'tm_sec', 'tm_wday', 'tm_yday', 'tm_isdst'])

#set ssl config 总是报SSL错误，没办法只能加上下面这句，不验证SSL了。
ssl._create_default_https_context = ssl._create_unverified_context
#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL, apikey, secretkey)
#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL, apikey, secretkey)
# zztest = okcoinFuture.future_ticker('btc_usd', 'this_week')['date']
# zztestt = okcoinFuture.future_ticker('btc_usd', 'this_week')['ticker']
column = ['date', 'high', 'vol', 'day_high', 'last', 'low', 'contract_id', 'buy', 'sell', 'coin_vol', 'day_low', 'unit_amount']
testdata = pd.DataFrame(columns=column)
i = 0
testdata.loc[testdata.shape[0]] = 1
print(testdata)
print(testdata.shape[0])
testdata.loc[testdata.shape[0]] = 2
print(testdata)
print(testdata.shape[0])
# testdata.loc[0] = [zztest]+list(zztestt.values())
# print(u' 期货行情')
# print(time.localtime(float(zztest)))
# print(pd.DataFrame(list(zztestp)).T)
# print(okcoinFuture.future_ticker('btc_usd', 'this_week'))
i += 1
print(i)
testdata.loc[testdata.shape[0]-1].to_csv('test.csv', index = None, sep = ',', mode = 'a+', encoding = 'utf-8')
print(testdata.loc[(testdata.shape[0]-1):(testdata.shape[0])])
