import requests
import configparser

Config=configparser.ConfigParser()
Config.read('config.ini')

def ConfigSectionMap(section):
    configDict = {}
    options = Config.options(section)
    for option in options:
        try:
            configDict[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
    return configDict

criteria=ConfigSectionMap('Acceptance Criteria')
endpointDict=ConfigSectionMap('Endpoint')


nameCheck=criteria['name']
promotionGalleryText=criteria['gallerydescriptiontext']
canRelistValue=Config.getboolean('Acceptance Criteria','canrelist')

endpoint=endpointDict['api']

def endpoint_setup():
    response=requests.get(endpoint)
    return response

api=endpoint_setup()
data=api.json()

endpointResponse=endpoint_setup().status_code

Promotions_Data= data['Promotions']

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
