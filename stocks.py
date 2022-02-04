import pandas as pd 
import numpy as np
import yfinance as yf
import requests as http
import time
import plotly.graph_objs as go

TICKER = 'SPY'

KEY = 'GQSAGBZTRBPRYACYABAH06ADCIAYCTX9' # don't make this public




data = yf.download(tickers=TICKER, period='1d', interval='1m')

print(data["Close"])