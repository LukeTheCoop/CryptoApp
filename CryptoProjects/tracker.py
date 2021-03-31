import requests
import csv
import threading
from time import sleep
import discord
import json

def check_currency(cur):
	CRYPTO = requests.get(f"https://api.coinstats.app/public/v1/coins/{cur}?currency=USD").json()
	if len(CRYPTO) == 0:
		return False
	else:
		return True

def get_currency(cur):
	CRYPTO = requests.get(f"https://api.coinstats.app/public/v1/coins/{cur}?currency=USD").json()

	price = round(CRYPTO['coin']['price'], 2)

	return price

#filtered = [item for item in mainDict['coins'] if item['name'] == 'Bitcoin']

#print(filtered)



if __name__ == '__main__':
	pass