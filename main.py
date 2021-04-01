import requests
import json
import time
import talib
import numpy
import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
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
	k_lines = bot.klines(symbol='BNBBTC', interval='5m', limit=200)

	inputs = {}
	inputs['open'] = numpy.asarray([float(i[1]) for i in k_lines])
	inputs['high'] = numpy.asarray([float(i[2]) for i in k_lines])
	inputs['low'] = numpy.asarray([float(i[3]) for i in k_lines])
	inputs['close'] = numpy.asarray([float(i[4]) for i in k_lines])

	sma = talib.SMA(inputs['close'])
	xdate = [datetime.datetime.fromtimestamp(item[0]/100) for item in k_lines]

	minutes = mdates.MinuteLocator()
	hours = mdates.HourLocator()
	timeFmt = mdates.DateFormatter('%H-%M')
	fig, ax = plt.subplots()
	plt.plot(xdate, sma)
	ax.xaxis.set_major_locator(hours)
	ax.xaxis.set_major_formatter(timeFmt)
	ax.xaxis.set_minor_locator(minutes)
	plt.show()


if __name__ == "__main__":
	main()
