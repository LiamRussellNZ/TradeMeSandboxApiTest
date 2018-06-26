#Name = "Carbon credits"
#CanRelist = true
#The Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"

import os
import requests
def endpoint_setup():
    response=requests.get('https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false')
    return response

api=endpoint_setup()
data=api.json()
print(api)

Promotions_Data= data['Promotions']

def check_ping():
    hostname = "www.google.co.nz"
    response = os.system("ping -n 1 " + hostname)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

def Promotions_test(Phrase):
	print('Testing if the promotions element with Name = "Gallery" has a description that contains the text "'+Phrase)
	for element in Promotions_Data:		
		for k in element.values():
			if k =='Gallery':
				elementDescription=element['Description']
				print('Testing if '+Phrase+' is in description')
				if Phrase in elementDescription:
					return True
				else:
					return False

def test_pingTest():
	assert check_ping()=="Network Active"

def test_endpointReachable():
	assert endpoint_setup().status_code==200
	print('Endpoint is reachable')


def test_name():
    print('Testing if name is equal to Carbon credits')
    assert data['Name']=='Carbon credits'

def test_canRelist():
	assert data['CanRelist']==True

def test_promotionsDescription():
	assert Promotions_test('2x larger image')==True 
	