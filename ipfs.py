import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE

	json_object = json.dumps(data, indent = 4) 
	
	files = {
		'file': json_object,
	}

	auth = ("2AW1mnzV6tcq27eNtvbTl3cgPXW","4db7b25efb64a0104b2ec86b7cc6ba77")

	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files = files, auth = auth)
	
	p = response.json()
	cid = p['Hash']

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	
	print(cid)
	
	params = (('arg', cid),)
	
	data = requests.post('https://ipfs.infura.io:5001/api/v0/block/cat', params=params)
	
	print(type(data))
	
	print("4")
	
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
