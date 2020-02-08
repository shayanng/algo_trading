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



#%% ATR