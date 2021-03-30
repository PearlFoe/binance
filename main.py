import requests
import json
import time
import websocket

from loguru import logger

from binance import Binance

def on_message(ws, message):
	data = json.loads(message)
	print(data)

def on_error(ws, error):
	print(error)

def on_close(ws):
	print("### closed ###")

def on_open(ws):
	print("### connected ###")

if __name__ == "__main__":
	#ws = websocket.WebSocketApp("wss://stream.binance.com:9443/stream?streams=ltcbtc@aggTrade/ethbtc@aggTrade",
	ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/ltcbtc@aggTrade/ethbtc@aggTrade",
								on_message = on_message,
								on_error = on_error,
								on_close = on_close)
	ws.on_open = on_open
	ws.run_forever()

'''
logger.add('main_log_file.log', format='{time} {level} {message}', level='INFO')
api_url = 'https://api.binance.com'

def get_api_keys(file_name):
	api_key = None 
	secret_key = None

	with open(file_name, 'rb') as f:
		data = json.loads(f.read())
		api_key = data['api_key']
		secret_key = data['secret_key']

	return api_key, secret_key

@logger.catch
def main():
	api_key, secret_key = get_api_keys('personal_data.json')
	bot = Binance(api_key, secret_key)
	account_info = bot.get_account_info(timestamp=bot.time()['serverTime'])
	print(account_info)

if __name__ == "__main__":
	main()
'''