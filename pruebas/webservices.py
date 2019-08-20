import requests
from pprint import pprint
import WS

r = WS.GET('http://localhost:8080/Employee/list.php')

# pprint(r.json())

for people in  r.json():
    print(people.get('code'))

