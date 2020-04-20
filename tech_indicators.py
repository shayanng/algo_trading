#%% MACD
import pandas_datareader.data as web
import datetime


ticker = "MSFT"

ohlcv = web.get_data_yahoo(ticker, datetime.date.today() - datetime.timedelta(1825), 
                           datetime.date.today())


def MACD(df, a, b, c):
    df = df.copy()
    df["MA_Fast"] = df["Adj Close"].ewm(span = a, min_periods = a).mean()
    df["MA_Slow"] = df["Adj Close"].ewm(span = b, min_periods = b).mean()
    df["MACD"] = df["MA_Fast"] - df["MA_Slow"]
    df["Signal"] = df["MACD"].ewm(span = c, min_periods = c).mean()
    df.dropna(inplace = True)
    return df

jj = MACD(ohlcv, 12, 26, 9)

#%% Bollinger Bands
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

ticker = "MSFT"

ohlcv = web.get_data_yahoo(ticker, datetime.date.today() - datetime.timedelta(1825), 
                           datetime.date.today())

def Bollinger_Bands(df, n):
    """
    this function calculates the bollinger bands
    """
    df = df.copy()
    df["MA"] = df['Adj Close'].rolling(n).mean()
    df["BB_up"] = df["MA"] + 2*df['Adj Close'].rolling(n).std(ddof=0)
    df["BB_dn"] = df["MA"] - 2*df['Adj Close'].rolling(n).std(ddof=0)
    df["BB_width"] = df["BB_up"] - df["BB_dn"]
    df.dropna(inplace=True)
    return df

# bband + plotting option
kk = Bollinger_Bands(ohlcv, 20)
kk.iloc[-100:,[-4,-3,-2]].plot(title="Bollinger Band")

#%% ATR
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

ticker = "MSFT"

ohlcv = web.get_data_yahoo(ticker, datetime.date.today() - datetime.timedelta(1825), 
                           datetime.date.today())

def ATR(df, n):
    df = df.copy()
    df['H-L'] = abs(df['High'] - df['Low'])
    df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))
    df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1))
    df['TR']=df[['H-L','H-PC','L-PC']].max(axis=1,skipna=False)
    df['ATR'] = df['TR'].rolling(n).mean()
    #df['ATR'] = df['TR'].ewm(span=n,adjust=False,min_periods=n).mean()
    df2 = df.drop(['H-L','H-PC','L-PC'],axis=1)
    return df2

### ATR Test + plotting option
jj = ATR(ohlcv, 10)
plt.style.use('ggplot')
plt.plot(jj[['ATR', 'TR']], alpha = 0.3)

