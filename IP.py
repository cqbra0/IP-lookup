import colorama
from colorama import Fore
import time
import json
import requests
print(f"""{Fore.BLUE}

╦┌─┐  ┬  ┌─┐┌─┐┬┌─┬ ┬┌─┐
║├─┘  │  │ ││ │├┴┐│ │├─┘
╩┴    ┴─┘└─┘└─┘┴ ┴└─┘┴  
\n\n""")

ip = input('Enter IP: ')
r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
geo = r.json()
fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
for field in fields:
  if field['value']:
    print(Fore.CYAN + field['name'] + ': ' + field['value'])
    time.sleep(0.2)
