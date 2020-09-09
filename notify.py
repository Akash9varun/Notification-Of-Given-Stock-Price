import streamlit as st
from yahoo_fin import stock_info
import time 
import pandas as pd 


st.title('Stock Alert Notification')
ticker = st.text_input('Enter The Ticker ')

if st.button('Get Current Price'):
    curr_price = int(stock_info.get_live_price(ticker))
    st.markdown('Current Price Of Stock Is ' + str(curr_price) )  


buy_price = st.text_input('Enter Buy Price')
sell_price = st.text_input('Enter Sell Price')

if st.button('Set Alert'):
    st.markdown('Stock Slert Monitoring Is On')
    while True:
            curr_price = int(stock_info.get_live_price(ticker))
            if curr_price < int(buy_price):
                st.markdown('BUY BUY BUY'+': Current Price Is'+ str(curr_price))
                break
            elif curr_price > int(buy_price):
                st.markdown('SELL SELL SELL'+': Current Price Is'+ str(curr_price))
                break
               
                
            time.sleep(3)
            
            
        



