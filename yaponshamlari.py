# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:05:11 2024

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
import numpy as np
import datetime

st.title('Tesla, Microsoft, Google va Amazon kompaniyalari aksiyalari narxi o\'zgarishi')

komp = st.radio(
    "Qaysi kompaniya tikerini tanlaysiz?",
   [":red[Tesla]", ":blue[Google]", ":green[Microsoft]", ":yellow[Amazon]"],
   captions = ["Tesla kompaniyasi", "Google kompaniyasi", "Microsoft kompaniyasi", "Amazon kompaniyasi"])
if komp== ":red[Tesla]":
    tiker = yf.Ticker('TSLA')
elif komp == ":blue[Google]":
    tiker = yf.Ticker('GOOG')
elif komp == ":green[Microsoft]":
    tiker = yf.Ticker('MSFT')
elif komp == ":yellow[Amazon]":
    tiker = yf.Ticker('AMZN')

d = st.date_input("Qachongan boshlab",
                  datetime.date(2023,12,1), max_value=datetime.date(2024,12,31),
                  min_value=datetime.date(2023,10,1))
st.write('Boshlanish vaqti', d)

prices = tiker.history(interval ='1d', start=d,)

prices

fig1=plt.figure()

#define witdth of the candlestick elements
width = 0.8
width2 = .1

#define up and down prices

up = prices[prices.Close > prices.Open]
down = prices[prices.Close < prices.Open]

#define colors to use
col2 = 'black'
col1 = 'steelblue'

#plot up prices
plt.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
plt.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
plt.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)

#plot down prices
plt.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
plt.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
plt.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)

#rotate X-axis tick labels
plt.xticks(rotation = 45, ha='right')

#display candlestick chart
fig1









        
   