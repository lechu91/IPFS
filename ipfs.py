import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	print("1")
	
	response = requests.post('https://ipfs.infura.io:5001/add', data = data)
	
	cid = response.text
	
	
	print("1.9")
	print(cid)
	print("2")

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	
	print("3")
	print(cid)
	
	params = (('arg', cid),)
	
	data = requests.post('https://ipfs.infura.io:5001/api/v0/block/cat', params=params)
	
	print("4")
	
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
