import requests
import json
import os
def get_capital(capital):
	
	url = 'https://jsonmock.hackerrank.com/api/countries?name=' +country
	payload={}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	r = json.loads(response.text.encode('utf8'))

	if r['total_pages'] == 0:
		print("-1")
	else:
		r = r['data']
		for name in r:
			 capital = name['capital']
	return capital

if __name__ == '__main__':
     fptr = open(os.environ['OUTPUT_PATH'], 'w')
     country = input('')
     result = get_capital(country)
     fptr.write(str(result) + '\n')
     fptr.close()


