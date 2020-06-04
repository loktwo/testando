#!/bin/python3
import requests
r = requests.get('https://google.com.br')
result = r.status_code
print(result)
