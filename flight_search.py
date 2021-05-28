from requests.models import RequestField, Response
import credential
import requests
import json
from pprint import pprint
import datetime

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
HEADERS = {"apikey": credential.GetTequilaAPIKey()}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        pass
    
    def SearchIATA(self, city_name):
        # print(city_name)
        params = {
            "term": city_name,
            "location_types": "city",              
        }
        
        response = requests.get(url= TEQUILA_ENDPOINT, headers= HEADERS, params= params)
        response.raise_for_status()
        result = response.json()
        
        IATACode = result['locations'][0]['code']
        
        return IATACode
    
    def SearchCheapFlight(self, fly_from, fly_to):
        '''
        The basic flights call could look like this: 
        https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021 
        https://tequila.kiwi.com/portal/docs/tequila_api/search_api
        
        dd/mm/YYYY, e.g. 29/05/2021
        '''
        
        today = datetime.datetime.now()
        tomorrow = today + datetime.timedelta(hours=24)
        six_months_from_tomorrow = tomorrow + datetime.timedelta(days=6*30)                
        seven_days_from_tomorrow = tomorrow + datetime.timedelta(days=7)
        twenty_eight_days_from_tomorrow = tomorrow + datetime.timedelta(days=28)
        
        #convert the format for the tequila API
        tomorrow = tomorrow.strftime("%d/%m/%Y")
        six_months_from_tomorrow =six_months_from_tomorrow.strftime("%d/%m/%Y")
        seven_days_from_tomorrow = seven_days_from_tomorrow.strftime("%d/%m/%Y")
        twenty_eight_days_from_tomorrow = twenty_eight_days_from_tomorrow.strftime("%d/%m/%Y")
        
        print(f"From: {fly_from} to {fly_to}")
        print(f"Departure date: {tomorrow}~{six_months_from_tomorrow} \nReturning date: {seven_days_from_tomorrow}~{twenty_eight_days_from_tomorrow}")
        
        #-----Input for request
        
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "dateFrom": tomorrow,
            "dateTo": six_months_from_tomorrow,
            "nights_in_dst_from": "7",
            "nights_in_dst_to" : "28",
            "curr": "USD",
        }
        
        response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, headers=HEADERS, params=params)
        response.raise_for_status()
        result = response.json()
        # pprint(result)
        
        prices = [flights['price'] for flights in result['data']]
        cheapest_flight = min(prices)
        print("Cheapest price: ", cheapest_flight)
        return cheapest_flight
    
    