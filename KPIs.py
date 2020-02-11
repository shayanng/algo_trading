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
spx["Adj Close"].plot()
plt.show()

def CAGR(df):
    df = df.copy()
    df["Daily Ret"] = df["Adj Close"].pct_change()
    df["Cum Return"] = (1 + df["Daily Ret"]).cumprod()
    CAGR = df["Cum Return"][-1]**(1/(len(df)/252)) - 1
    return CAGR

cagr_tst = CAGR(spx)
print(cagr_tst)

#%%