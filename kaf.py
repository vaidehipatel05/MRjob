from kafka import KafkaProducer
import json
import creds
from datetime import datetime, timedelta
from time import sleep
import requests
from alpaca_trade_api import REST, TimeFrame

api_key = creds.PUBLIC_KEY
secret_key = creds.SECRET_KEY
base_url = "https://paper-api.alpaca.markets"

end_date = datetime.today() - timedelta(days=1)
start_date = end_date - timedelta(days=365 * 2)

symbols = ['MMM']

producer = KafkaProducer(bootstrap_servers='localhost:9092')

api = REST(key_id=api_key, secret_key=secret_key,
           base_url=base_url, api_version='v2')


def fetch_data_from_api():
    df_barset = api.get_bars(symbols, TimeFrame.Day, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'),
                          adjustment='all').df
    df_barset = df_barset.reset_index(level=0)

    #print(df_barset.to_json())
    # response = requests.get('your_api_endpoint')
    return df_barset.to_json()


def publish_data():
    data = fetch_data_from_api()
    producer.send('MarketData', json.dumps(data).encode('utf-8'))
    print(json.dumps(data).encode('utf-8'))


publish_data()

