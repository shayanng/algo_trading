#%%  Imports
import pandas_datareader.data as web
import datetime 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# %% getting stock data
ticker = "AMZN"

start_date = datetime.date.today() - datetime.timedelta(365)
end_date = datetime.date.today()

data_daily = web.get_data_yahoo(ticker, start_date, end_date) 
data_monthly = web.get_data_yahoo(ticker, start_date, end_date, interval = 'm') 
data_weekly = web.get_data_yahoo(ticker, start_date, end_date, interval = 'wk')
#data = web.DataReader(ticker, "quandl", start_date, end_date)

#%% preparation

# Import necesary libraries
import pandas as pd
import pandas_datareader.data as web
import datetime


tickers = ["ASIANPAINT.NS","ADANIPORTS.NS","AXISBANK.NS","BAJAJ-AUTO.NS",
           "BAJFINANCE.NS","BAJAJFINSV.NS","BPCL.NS","BHARTIARTL.NS",
           "INFRATEL.NS","CIPLA.NS","COALINDIA.NS","DRREDDY.NS","EICHERMOT.NS",
           "GAIL.NS","GRASIM.NS","HCLTECH.NS","HDFCBANK.NS","HEROMOTOCO.NS",
           "HINDALCO.NS","HINDPETRO.NS","HINDUNILVR.NS","HDFC.NS","ITC.NS",
           "ICICIBANK.NS","IBULHSGFIN.NS","IOC.NS","INDUSINDBK.NS","INFY.NS",
           "KOTAKBANK.NS","LT.NS","LUPIN.NS","M&M.NS","MARUTI.NS","NTPC.NS",
           "ONGC.NS","POWERGRID.NS","RELIANCE.NS","SBIN.NS","SUNPHARMA.NS",
           "TCS.NS","TATAMOTORS.NS","TATASTEEL.NS","TECHM.NS","TITAN.NS",
           "UPL.NS","ULTRACEMCO.NS","VEDL.NS","WIPRO.NS","YESBANK.NS","ZEEL.NS"]

stock_cp = pd.DataFrame() 
attempt = 0
drop = []
while len(tickers) != 0 and attempt <= 5:
    tickers = [j for j in tickers if j not in drop] 
    for i in range(len(tickers)):
        try:
            temp = web.get_data_yahoo(tickers[i],datetime.date.today()
                                      -datetime.timedelta(1095),
                                      datetime.date.today())
            
            temp.dropna(inplace = True)
            stock_cp[tickers[i]] = temp["Adj Close"]
            drop.append(tickers[i])       
        except:
            print(tickers[i]," :failed to fetch data...retrying")
            continue
    attempt+=1

#%%4
from yahoofinancials import YahooFinancials

ticker = 'AAPL'
yahoo_financials = YahooFinancials(ticker)
historical_stock_prices = yahoo_financials.get_historical_price_data('2015-09-15', 
                                                                     '2020-02-03',
                                                                     'daily')






