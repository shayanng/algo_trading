import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
plt.style.use("ggplot")


tickers = ["AAPL", "AMZN", "MSFT", "CSCO", "IBM", "FB"]

close_price = pd.DataFrame()
attempts = 0
drop = []
while len(tickers) != 0 and attempts <= 5:
    tickers = [j for j in tickers if j not in drop]
    for i in range(len(tickers)):
        try:
            temp = web.get_data_yahoo(tickers[i],
                                      datetime.date.today() - datetime.timedelta(3650),
                                      datetime.date.today())
           
            temp.dropna(inplace = True)
            close_price[tickers[i]] = temp["Adj Close"]
            drop.append(tickers[i])
        except:
            print(tickers[i], " :failed to fetch data...retrying")
            continue
    attempts += 1
        
## handling NaN value
close_price.fillna(method = "bfill", axis = 0, inplace = True)
close_price_mean = close_price.mean()
close_price_median = close_price.median()
close_price_std = close_price.std() 
    
daily_return = close_price.pct_change()
daily_return_mean = daily_return.mean()

ma20 = daily_return.rolling(window = 20).mean() #simple moving average
std20 = daily_return.rolling(window = 20, min_periods = 20).std() 

ema20 = daily_return.ewm(span = 20, min_periods = 20).mean()


## visualization
plt.figure(figsize = (12,8))
cp_standardized = (close_price - close_price.mean())/close_price.std()
cp_standardized.plot();


plt.figure(figsize = (12,8))
sns.lineplot(data = cp_standardized)


close_price.plot(subplots = True, layout = (3,2),
                 title = 'stock price evolution', grid = True)

plt.style.available
plt.style.use("ggplot")

sns.countplot(close_price['AAPL'])
sns.boxenplot(data = close_price)
sns.lmplot(data = close_price)

plt.bar(daily_return.columns, daily_return_mean)

## Matplotlib.pyplot Object Oriented approach
fig, ax = plt.subplots()
ax.set(title = "daily return on tech stocks",
       xlabel = "tech stocks", ylabel = "daily return")
plt.bar(daily_return.columns, daily_return_mean)


