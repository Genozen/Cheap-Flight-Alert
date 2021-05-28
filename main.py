import data_manager as DM
import flight_data as FD
import flight_search
from pprint import pprint

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


#------------------Test google sheet with sheetly

sheetly = DM.DataManager()
sheet_data = sheetly.Get() #Gets the spread sheet back

#-------------------Check if IATA Code is empty, if empty send it to flight_search and complete the sheet

flight_search = flight_search.FlightSearch()

# for row in range(0, len(sheet_data['flight'])):
#     entry_info = sheet_data['flight'][row]
#     #If no IATA Code found in that city, pass to flight_search and return TESTING
#     if len(entry_info['iataCode']) == 0:
#         city_name = entry_info['city']
#         sheet_data['flight'][row]['iataCode'] = flight_search.SearchIATA(city_name)

# sheetly.Put(sheet_data)

#------------------Search for cheap flights
flight_data = FD.FlightData()

for row in sheet_data['flight']:
    flight_search.SearchCheapFlight("LON",row['iataCode'])


