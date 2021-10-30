import numpy as np
import pandas as pd
import csv
import requests
import json
import math 
#author: David Gae © 2021 david gae Some right reserved


def generation(r):
	date  =[]
	hospitalizedIncr = []
	negative = []
	negativeIncr = []
	positive = []
	positiveIncr = []
	totalTestResults = []
	file1 = open('federal_covid19.csv', 'r')
	# Identify nearest city for each lat, lng combination
	file = csv.DictReader(file1)
	for col in file:
		#date.append(col['date'])
		hospitalizedIncr.append(col['hospitalizedIncrease'])
		negative.append(col['negative'])
		negativeIncr.append(col['negativeIncrease'])
		positive.append(col['positive'])
		positiveIncr.append(col['positiveIncrease'])
		totalTestResults.append(col['totalTestResults'])

	hospitalincrease = [int(integer) for integer in hospitalizedIncr]
	#hospitalincrease2 = np.sum(hospitalincrease)
	#a = len(date)
	b = len(hospitalizedIncr)
	c = len(negative)
	d = len(negativeIncr)
	e = len(positive)
	f = len(positiveIncr)
	h = len(totalTestResults)
	data = {
		 	"hospitalizedIncrease": hospitalincrease[0] ,
		 	"negative":  int(negative[1]),
		 	"positive": int(positive[1]),
	       }
	#print(data)
	return data

def api_data(data):
	# initial counters for log and sets
	#df =pd.DataFrame(data.items())
	df = data
	basic_url = "https://api.covidtracking.com/v1/us/current.json"
	js = requests.get(basic_url).json()
	for js1 in js:
		#print(js1)
		if js1['negative'] > df['negative']:
			print( "COVID19tracking.com negative:",js1['negative'])
			print("Federal data negative:", df['negative'])
			print("MORE COVID19 CASES")
			print('-------------------------------')
		if js1['positive'] > df['positive']:
			print( "COVID19tracking.com positive:",js1['positive'])
			print("Federal data positive:", df['positive'])
			print("MORE COVID19 POSITIVE")
			print('-------------------------------')
		if js1['hospitalizedIncrease'] > df['hospitalizedIncrease']:
			print( "COVID19tracking.com hospital cases:",js1['hospitalizedIncrease'])
			print("Federal data hospital cases:", df['hospitalizedIncrease'])
			print("more nurses on staff/call")

	data2 = { 'negative': js1['negative'],
			  'positive': js1['positive'],
			  'hopsitalizedIncreases': js1['hospitalizedIncrease'],
			}

	df = pd.DataFrame(data2.items())
	print('-------------------------------')
	print('Data Retrieval Complete and "Checked"')
	print('-------------------------------')
	df.to_csv('covid19current_Dataset.csv', sep=',', encoding='utf-8')

if __name__ == '__main__':
	r =generation(1)
	#print(r)
	z = api_data(r)
	print(r)
