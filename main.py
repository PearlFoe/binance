import requests
import json
import time

from loguru import logger

from binance import Binance

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


if __name__ == '__main__':
	main()