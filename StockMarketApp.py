import streamlit as st
import yfinance as yf
import datetime
import mplfinance as mpf

col1, col2, col3 = st.columns(3)

with col1:
    ticker_symbol = st.text_input("Stock name")

with col2:
    start_date = st.date_input("Start Date", value = datetime.date(2019, 1, 7))

with col3:
    end_date = st.date_input("End Date", value = datetime.date(2023, 1, 7))


data = yf.download(ticker_symbol, start=start_date, end=end_date)

st.write(data)

st.line_chart(data['Close'])
st.bar_chart(data['Volume'])


