#!/usr/bin/env python
# coding: utf-8

# In[56]:


import yfinance as finance
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# In[57]:


from_date = '1987-01-01'
today = datetime.now()

raw_ticker = [input(),input(),input()]

ticker_with_space = [x.upper() for x in raw_ticker]

ticker = [x.strip(' ') for x in raw_ticker]

stock = finance.download(ticker, from_date, today)

# stock.tail()
# stock()

stock['Adj Close'].plot(figsize=(15, 8))


plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)

plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

plt.show()

data = pd.DataFrame(columns=raw_ticker)

for ticker in raw_ticker:
    data[ticker] = finance.download(ticker, 
                               from_date,
                               today)['Adj Close']
    
data.tail()

# In[58]:


# data = pd.DataFrame(columns=raw_ticker)

# for ticker in raw_ticker:
#     data[ticker] = finance.download(ticker, 
#                                from_date,
#                                today)['Adj Close']
    
# data.head()


# In[59]:


#  print(stock)


# In[60]:


# pd.DataFrame(stock)


# In[ ]:




