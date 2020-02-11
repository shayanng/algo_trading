#%% Compounded Annual Growth Rate (CAGR)

# CAGR = [end value/beginning value]^(1/years) - 1 

import pandas_datareader.data as web
import numpy as np
import datetime
import matplotlib.pyplot as plt
plt.style.use('ggplot')

ticker = "^GSPC"

spx = web.get_data_yahoo(ticker, 
                        datetime.date.today() - datetime.timedelta(1825),
                        datetime.date.today())

plt.figure(figsize = (12,8))
spx["Adj Close"].plot(color = "blue")
plt.show()

def CAGR(df):
    df = df.copy()
    df["Daily Ret"] = df["Adj Close"].pct_change()
    df["Cum Return"] = (1 + df["Daily Ret"]).cumprod()
    CAGR = df["Cum Return"][-1]**(1/(len(df)/252)) - 1
    return CAGR

cagr_tst = CAGR(spx)
print(cagr_tst)

#%% Annualized volatility 
import pandas_datareader.data as web
import numpy as np
import datetime

ticker = "^GSPC"

spx = web.get_data_yahoo(ticker, 
                        datetime.date.today() - datetime.timedelta(1825),
                        datetime.date.today())

def annualized_volatility(df):
    df = df.copy()
    df["Daily Ret"] = df["Adj Close"].pct_change()
    vol = df["Daily Ret"].std() * np.sqrt(256)
    return vol

av_tst = annualized_volatility(spx)

#%% Sharpe & Sortino Ratio
import pandas_datareader.data as web
import numpy as np 
import datetime

ticker = "^GSPC"

spx = web.get_data_yahoo(ticker, 
                        datetime.date.today() - datetime.timedelta(1825),
                        datetime.date.today())

## before the calcultion of sharpe ratio we must have the risk-free rate
risk_free_rate = 0.022

def sharpe_ratio(df, rfr):
    df = df.copy()
    sr = (CAGR(df) - rfr)/annualized_volatility(df)
    return sr

def sortino_ratio(df, rfr):
    df["Daily Ret"] = df["Adj Close"].pct_change()
    neg_vol = df[df["Daily Ret"] < 0]["Daily Ret"].std() * np.sqrt(256)
    sor = (CAGR(df) - rfr)/neg_vol
    return sor
    
    
sr_tst = sharpe_ratio(spx, risk_free_rate)  
sor_tst = sortino_ratio(spx, risk_free_rate)

#%% Max Drawdown & Calmar Ratio
import pandas_datareader.data as web
import numpy as np 
import datetime

ticker = "^GSPC"

spx = web.get_data_yahoo(ticker, 
                        datetime.date.today() - datetime.timedelta(365*15),
                        datetime.date.today())

plt.style.use("ggplot")
spx["Adj Close"].plot(figsize = (12,8), color = "red")

def max_drawdown(df):
    df = df.copy()
    df["Daily Ret"] = df["Adj Close"].pct_change()
    df["Cum Return"] = (1 + df["Daily Ret"]).cumprod()
    df["Cum Rolling Max"] = df["Cum Return"].cummax()
    df["Drawdown"] = df["Cum Rolling Max"] - df["Cum Return"]
    df["Drawdown_Pct"] = df["Drawdown"] / df["Cum Rolling Max"]
    max_dd = df["Drawdown"].max()
    return max_dd

def calmar_ratio(df):
    df = df.copy()
    calmar = CAGR(df)/max_drawdown(df)
    return calmar

cal_tst = calmar_ratio(spx)
dd_tst = max_drawdown(spx)






