import time
import requests
import hmac, hashlib
from urllib.parse import urlencode

class Binance():
	"""docstring for Binance"""
	def __init__(self, api_key, secret_key):
		self.API_KEY = api_key
		self.SECRET_KEY = secret_key
		self.headers = {
					"X-MBX-APIKEY": self.API_KEY, 
					"Content-Type":"application/x-www-form-urlencoded"
		}

	def hashing(self, string):
		return hmac.new(self.SECRET_KEY.encode('utf-8'), string.encode('utf-8'), hashlib.sha256).hexdigest()

	def ping(self):
		url = 'https://api.binance.com/api/v1/ping'
		response = requests.get(url)
		return response.json()
	
	def time(self):
		url = 'https://api.binance.com/api/v1/time'
		response = requests.get(url)
		return response.json()

	def exchange_info(self, **kwargs):
		url = 'https://api.binance.com/api/v1/exchangeInfo'
		response = requests.get(url, params=kwargs)
		return response.json()


	def depth(self, **kwargs):
		'''
		Позволяет получить книгу открытых ордеров
		на бирже.
		Параметры: 
		symbol - обязателен
		limit - необязателен
		'''
		url = ' https://api.binance.com/api/v1/depth'
		response = requests.get(url, params=kwargs)
		return response.json()

	def trades(self, **kwargs):
		'''
		Позволяет получить Последние (чужие) сделки.
		Параметры: 
		symbol - обязателен
		limit - необязателен
		'''
		url = ' https://api.binance.com/api/v1/trades'
		response = requests.get(url, params=kwargs)
		return response.json()

	def klines(self, **kwargs):
		'''
		Позволяет получить данные по свечам.
		Параметры:
		symbol - обязателен
		interval - обязателен
		limit - необязателен
		startTime - необязателен
		endTime - необязателен
		'''
		url = ' https://api.binance.com/api/v1/klines'
		response = requests.get(url, params=kwargs)
		return response.json()

	def ticker(self, symbol):
		'''
		Позволяет получить статистику за 24 часа.
		'''
		url = 'https://api.binance.com/api/v3/ticker/24hr'
		params = {'symbol':symbol}
		response = requests.get(url, params=params)
		return response.json()

	def ticker_price(self, symbol=None):
		'''
		Позволяет поулчить последнюю цена по паре (или парам).
		'''
		url = 'https://api.binance.com/api/v1/ticker/price'
		params = {'symbol':symbol}
		response = requests.get(url, params=params)
		return response.json()		 

	def book_tiker(self, symbol=None):
		'''
		Позволяет получить лучшие цены покупки/продажи.
		'''
		url = 'https://api.binance.com/api/v3/ticker/bookTicker'
		params = {'symbol':symbol}
		response = requests.get(url, params=params)
		return response.json()

	def create_order(self, **kwargs):
		'''
		Создание ордера.
		'''
		url = 'https://api.binance.com/api/v3/order'
		params = kwargs
		signature = self.hashing(urlencode(kwargs).replace('%27', '%22'))
		params['signature'] = signature

		response = requests.post(url, params=params, headers=self.headers)
		return response.json()

	def get_order_info(self, **kwargs):
		'''
		Получение информации об ордере.
		'''
		url = 'https://api.binance.com/api/v3/order'
		params = kwargs
		signature = self.hashing(urlencode(kwargs).replace('%27', '%22'))
		params['signature'] = signature

		response = requests.get(url, params=params, headers=self.headers)
		return response.json()

	def delete_order(self, **kwargs):
		'''
		Отмена ордера
		'''
		url = 'https://api.binance.com/api/v3/order'
		params = kwargs
		signature = self.hashing(urlencode(kwargs).replace('%27', '%22'))
		params['signature'] = signature

		response = requests.delete(url, params=params, headers=self.headers)
		return response.json()

	def get_open_orders(self, **kwargs):
		'''
		Получение информации об открытых ордерах.
		'''
		url = 'https://api.binance.com/api/v3/openOrders'
		params = kwargs
		signature = self.hashing(urlencode(kwargs).replace('%27', '%22'))
		params['signature'] = signature

		response = requests.get(url, params=params, headers=self.headers)
		return response.json()

	def get_all_orders(self, **kwargs):
		'''
		Полчение информации об всех ордерах, в том числе
		и об отмененных и закрытых.
		'''
		url = 'https://api.binance.com/api/v3/allOrders'
		params = kwargs
		signature = self.hashing(urlencode(kwargs).replace('%27', '%22'))
		params['signature'] = signature

		response = requests.get(url, params=params, headers=self.headers)
		return response.json()

	def get_account_info(self, **kwargs):
		'''
		Получение информации об аккаунте.
		'''
		url = 'https://api.binance.com/api/v3/account'
		params = kwargs
		signature = self.hashing(urlencode(kwargs).replace('%27', '%22'))
		params['signature'] = signature

		response = requests.get(url, params=params, headers=self.headers)
		return response.json()

	def get_trades(self, **kwargs):
		'''
		Позволяет получить историю торгов по указанной паре.
		'''
		url = 'https://api.binance.com/api/v3/myTrades'
		params = kwargs
		signature = self.hashing(urlencode(kwargs).replace('%27', '%22'))
		params['signature'] = signature

		response = requests.get(url, params=params, headers=self.headers)
		return response.json()