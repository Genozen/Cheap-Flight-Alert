import requests
import json
from pprint import pprint


from requests.models import Response
import credential

ENDPOINT = "https://api.sheety.co/ad05316c37fdbce7984dfb63b2c1d8db/flightSheet/flight"
api_key = credential.GetSheetlyAPIKey()
app_id = credential.GetSheetlyAppID()
token = credential.GetSheetlyToken()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    
    def Get(self):
        response = requests.get(url=ENDPOINT,headers=token)
        result = response.json()
        self.destination_data = result
        # pprint(result)
        return result
    
    def Post(self, sheet_data):
        #Not sure why, but the column names returned are assigned to lwoer case.
        #probably mentioned in the document
        #IATA code is the airport code
        params = {
            "flight":{
                "city": "Sample",
                "iataCode": "abc",
                "lowestPrice": "0"
            }
        }
        response = requests.post(url=ENDPOINT, json=params , headers=token)
        result = response.json()
        print(result)
        

    def Put(self, sheet_data):
        
        for row in range(0, len(sheet_data['flight'])):
            entry_info = sheet_data['flight'][row]
            row_id = entry_info['id']
            row_Endpoint = ENDPOINT+"/"+str(row_id)
            
            params = {
                "flight":{
                    "city": entry_info['city'],
                    "iataCode": entry_info['iataCode'],
                    "lowestPrice": entry_info['lowestPrice'],
                }
            }
            
            response = requests.put(url=row_Endpoint, json=params , headers=token)
        
        print("Chart updated")
