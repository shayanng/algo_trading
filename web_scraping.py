#web scrapping
#%%
import pandas as pd
a = 2
b = 3

import requests
from bs4 import BeautifulSoup

url = 'https://ca.finance.yahoo.com/quote/TSLA/balance-sheet?p=TSLA'
page = requests.get(url)