#Analysing the Cryptocurrency of May 2021 | Python for Finance basics
#https://www.analyticsvidhya.com/blog/2021/05/analyzing-the-cryptocurrency-of-may-2021-python-for-finance-basics/
import warnings
warnings.filterwarnings('ignore')  # Hide warnings
import datetime as dt
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.dates as mdates

import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'

start = dt.datetime(2021, 1, 1)
end = dt.datetime(2021,5,29)

btc = web.DataReader("BTC-USD", 'yahoo', start, end)  # Collects data
btc.reset_index(inplace=True)

#bitcoin

crypto= btc[['Date','Adj Close']]
crypto= crypto.rename(columns = {'Adj Close':'BTC'})

# 7 day moving average

crypto[ 'BTC_7DAY_MA' ] = crypto.BTC.rolling( 7).mean()

#Ethereum

eth = web.DataReader("ETH-USD", 'yahoo', start, end)  # Collects data
eth.reset_index(inplace=True)
crypto["ETH"]= eth["Adj Close"]

# 7 day moving average
crypto[ 'ETH_7DAY_MA' ] = crypto.ETH.rolling( 7).mean()

#doge coin

doge = web.DataReader("DOGE-USD", 'yahoo', start, end)  # Collects data
doge.reset_index(inplace=True)
crypto["DOGE"]= doge["Adj Close"]

# 7 day moving average
crypto[ 'DOGE_7DAY_MA' ] = crypto.DOGE.rolling( 7).mean()

#BinanceCoin 

bnb = web.DataReader("BNB-USD", 'yahoo', start, end)  # Collects data
bnb.reset_index(inplace=True)
crypto["BNB"]= bnb["Adj Close"]

# 7 day moving average
crypto[ 'BNB_7DAY_MA' ] = crypto.BNB.rolling( 7).mean()

#Cardano

ada = web.DataReader("ADA-USD", 'yahoo', start, end)  # Collects data
ada.reset_index(inplace=True)
crypto["ADA"]= ada["Adj Close"]


# 7 day moving average
crypto[ 'ADA_7DAY_MA' ] = crypto.ADA.rolling( 7).mean()

#XRP

xrp = web.DataReader("XRP-USD", 'yahoo', start, end)  # Collects data
xrp.reset_index(inplace=True)
crypto["XRP"]= xrp["Adj Close"]

# 7 day moving average
crypto[ 'XRP_7DAY_MA' ] = crypto.XRP.rolling( 7).mean()

#Dash

dash = web.DataReader("DASH-USD", 'yahoo', start, end)  # Collects data
dash.reset_index(inplace=True)
crypto["DASH"]= dash["Adj Close"]

# 7 day moving average

#getting the dates 

crypto.set_index("Date", inplace=True)

crypto[['BTC','ETH','DOGE','BNB','ADA','XRP','DASH']].head()

crypto[['BTC','ETH','DOGE','BNB','ADA','XRP','DASH']].corr()

#heatmap

plt.figure(figsize = (5,5))
sns.heatmap(crypto[['BTC','ETH','DOGE','BNB','ADA','XRP','DASH']].corr(),annot=True, cmap='YlOrRd_r')

fig = px.line(crypto, y=["BTC",'ETH','DOGE','BNB','ADA','XRP','DASH'] )
fig.show()

fig = px.line(crypto, y=['BTC_7DAY_MA'],title='BTC-USD in 7 Days MA Line' )
fig.show()

fig = px.line(crypto, y=['ETH'],title='ETH-USD Price' )
fig.show()

fig = px.line(crypto, y=['ETH_7DAY_MA'],title='ETH in 7 Days MA Line' )
fig.show()

fig = px.line(crypto, y=['DOGE'],title='Doge-USD Price' )
fig.show()


fig = px.line(crypto, y=['DOGE_7DAY_MA'], title='Doge in 7 Days MA Line' )
fig.show()

