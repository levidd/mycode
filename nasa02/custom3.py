#!/usr/bin/env python3

import requests

url = "http://api.open-notify.org/astros.json"

r = requests.get(url).json().get("people")

print("People in space:", len(r))
for person in r:
    print(person.get('name'), "on the", person.get('craft'))


