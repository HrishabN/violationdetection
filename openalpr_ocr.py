import requests
import base64
import json

def ocr(IMAGE_PATH):
	try:
                with open(IMAGE_PATH, 'rb') as fp:
                    response = requests.post(
                        'https://api.platerecognizer.com/v1/plate-reader/',
                        files=dict(upload=fp),
                        headers={'Authorization': 'Token 3760e06d55187d0cd6f25f1243b932813590c431'})
                results = response.json()
                return results['results'][0]['plate']
		
	except:
		print("No number plate found")
