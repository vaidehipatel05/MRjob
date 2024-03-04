from kafka import KafkaConsumer

bootstrap_servers = 'localhost:9092'
topic = 'MarketData'
print("Started")

consumer = KafkaConsumer(topic,
                         bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='earliest',
                         group_id='market_data_consumer_group')

for message in consumer:
    market_data = message.value.decode('utf-8')
    print("Received market data:", market_data)

print("Waiting for the msg")
consumer.close()