import sys
import json
import pandas as pd
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python  show_bus_locations_amm1209.py YourKeyHere BusLineHere")
    sys.exit()

KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+KEY+'&VehicleMonitoringDetailLevel=calls&LineRef='+BUS_LINE

response = urllib.urlopen(url)
d = response.read().decode("utf-8")
d = json.loads(d)

#with open('data'+BUS_LINE+'.json', 'w') as outfile:
    #json.dump(d, outfile)

bus_line = d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']

n_buses = len(d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print('Bus line: '+bus_line)
print('Number of buses: '+str(n_buses))

for i in range(n_buses):
	latitude = d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	longitude = d['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	print('Bus '+str(i+1)+' is at latitude: '+str(latitude)+' and longitude: '+str(longitude))