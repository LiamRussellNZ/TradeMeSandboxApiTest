#Name = "Carbon credits"
#CanRelist = true
#The Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"

import requests
response=requests.get('https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false')
print(response)
data=response.json()

Promotions_Data= data['Promotions']

def Promotions_test(Phrase):
	print('Testing if the promotions element with Name = "Gallery" has a description that contains the text "2x larger image"')
	for element in Promotions_Data:		
		for k in element.values():
			if k =='Gallery':
				elementDescription=element['Description']
				print('Testing if '+Phrase+' is in description')
				if Phrase in elementDescription:
					return True
				else:
					return False

def test_name():
	assert data['Name']=='Carbon credits'

def test_canRelist():
	assert data['CanRelist']==True

def test_promotionsDescription():
	assert Promotions_test('Does this work')==True #'2x larger image'