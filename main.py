try:
	import os
	import requests

	url= 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'


	def endpoint_setup():
		response=requests.get(url)
		return response

	api=endpoint_setup()
	data=api.json()

	endpointResponse=endpoint_setup().status_code
	nameCheck='Carbon credits'

	Promotions_Data= data['Promotions']

	#Promotions has element with Name = "Gallery" has a Description that contains the text "2x larger image"
	promotionGalleryText='2x larger image'

	canRelistValue=True

	def Promotions_test(Phrase):
		print('Testing if the promotions element with Name = "Gallery" has a description that contains the text "'+Phrase)
		for element in Promotions_Data:		
			for k in element.values():
				if k =='Gallery':
					elementDescription=element['Description']
					if Phrase in elementDescription:
						return True
					else:
						return False

	def test_endpointReachableSends200():
		assert endpointResponse==200
		print('Endpoint returns '+str(endpointResponse))

	def test_name():
		print('Testing if name is equal to '+nameCheck)
		assert data['Name']==nameCheck

	def test_canRelist():
		print('Testing if CanRelist element is set to '+str(canRelistValue))
		assert data['CanRelist']==canRelistValue

	def test_promotionsDescription():
		assert Promotions_test(promotionGalleryText)==True 

except:
	print("Some went wrong")