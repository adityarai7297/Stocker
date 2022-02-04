import pandas as pd 
import requests as http
import time

TICKER = 'SPY'
URL = 'https://api.tdameritrade.com/v1/marketdata/'+ TICKER +'/quotes'
KEY = 'GQSAGBZTRBPRYACYABAH06ADCIAYCTX9' # don't make this public
PAYLOAD = {'apikey': KEY}

i=1
while(i<10):
    response = http.get(URL, params = PAYLOAD)
    info = response.json()
    print(float(info[TICKER]['closePrice']))
    i+=1
    time.sleep(60)