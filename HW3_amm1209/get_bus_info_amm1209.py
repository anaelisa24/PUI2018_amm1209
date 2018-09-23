
import sys
import json
import pandas as pd
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python  show_bus_locations_amm1209.py YourKeyHere BusLineHere")
    sys.exit()

KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
CSV_NAME = sys.argv[3]

#KEY = '8d49ea8c-9b0e-41f2-a7a3-f47de0eddf79'

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+KEY+'&VehicleMonitoringDetailLevel=calls&LineRef='+BUS_LINE

response = urllib.urlopen(url)
d = response.read().decode("utf-8")
d = json.loads(d)

#with open('data'+BUS_LINE+'.json', 'w') as outfile:
    #json.dump(d, outfile)

file = open(CSV_NAME, "w")

bus_line = d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']

n_buses = len(d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

file.write('Latitude,Longitude,Stop Name,Stop Status\n')
for i in range(n_buses):
	latitude = d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	longitude = d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	stop_name = d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
	stop_status = d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
	file.write(str(latitude)+','+str(longitude)+','+str(stop_name)+','+str(stop_status)+'\n')



