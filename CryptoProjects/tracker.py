import requests
import csv
import threading
from time import sleep
import json
import pickle
import threading

def check_data():
	try:
		with open('TRACKED_CURRENCYS.pkl', 'rb') as pickle_file:
			pickle.load(pickle_file)
	except:
		clear_tracked_list()


def get_tracked_list():
	with open('TRACKED_CURRENCYS.pkl', 'rb') as pickle_file:
		tracked_list = pickle.load(pickle_file)

	return tracked_list

def clear_tracked_list():
	with open('TRACKED_CURRENCYS.pkl', 'wb') as pickle_file:
		pickle.dump([], pickle_file)

def check_goal(item):
	crypto, target, greater = item.split('-')[0], item.split('-')[1], item.split('-')[2]

	crypto = get_currency(crypto)

	if greater == '1':
		if float(crypto) >= float(target):
			return True
		else:
			return False
	else:
		if float(crypto) <= float(target):
			return True
		else:
			return False


def remove_track(input):
	tracked_list = get_tracked_list()

	tracked_list.remove(tracked_list[input])

	with open('TRACKED_CURRENCYS.pkl', 'wb') as pickle_file:
		pickle.dump(tracked_list, pickle_file)
		

def add_track(cur, target):
	tracked_list = get_tracked_list()
	greater = 0

	price = get_currency(cur)

	if float(price) > float(target):
		greater = 0
	else:
		greater = 1

	temp = str(cur) + '-' + str(target) + '-' + str(greater)


	tracked_list += [temp]

	with open('TRACKED_CURRENCYS.pkl', 'wb') as pickle_file:
		pickle.dump(tracked_list, pickle_file)


def check_currency(cur):
	try:
		CRYPTO = requests.get("https://api.coinstats.app/public/v1/coins/" + cur + "?currency=USD").json()

	except: #No internet if except 
		return True 

	return True

def get_currency(cur):
	try:
		CRYPTO = requests.get("https://api.coinstats.app/public/v1/coins/" + cur + "?currency=USD").json()
		price = round(CRYPTO['coin']['price'], 2)
		return price

	except:
		if cur == 'bitcoin':
			price = 59482.82
		elif cur == 'cardano':
			price = 1.21
		elif cur == 'dogecoin':
			price = 0.2

		return price



if __name__ == '__main__':
	clear_tracked_list()



