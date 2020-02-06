#web scrapping
#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup

tickers = ['AAPL', 'MSFT']
financial_dir = {}

for ticker in tickers:
    temp_dir = {}
    url = 'https://ca.finance.yahoo.com/quote/'+ticker+'/balance-sheet?p='+ticker
    page = requests.get(url)    
    page_content = page.content
    soup = BeautifulSoup(page_content, 'html.parser')
    table = soup.find_all("div", {"class" : "M(0) Mb(10px) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in table:
        rows = t.find_all("div", {"class" : "rw-expnded"})
        for row in rows:
            temp_dir[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[1]

#%%
            