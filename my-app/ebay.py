import requests
import json

# set up the request parameters
params = {
  'api_key': 'C9A8A5376E3647BF9EECCA55D08DA93D',
  'type': 'search',
  'ebay_domain': 'ebay.com',
  'search_term' : 'cards'
}

# make the http GET request to Countdown API
api_result = requests.get('https://api.countdownapi.com/request', params)

# print the JSON response from Countdown API
print(json.dumps(api_result.json()))