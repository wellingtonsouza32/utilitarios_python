#Import bibliotecas
import requests
import csv
import urllib3
import json
from  itertools import zip_longest

#disable Warnings https
urllib3.disable_warnings()

#logic
headers = {"accept": "application/json"}
page = 0
idexport = []
nameexport = []

for page in range(0,501):
    url = "xxxxxxxxx&page="+ str(page)
    print(page)
    response = requests.get(url, headers=headers,verify=False)
    res = json.loads(response.text)
    for contacts in res['contacts']:
        idexport.append(contacts["id"])
        nameexport.append(contacts["name"])
        d = [idexport, nameexport]
        export_data = zip_longest(*d, fillvalue = '')
        #exportar csv
        with open('jsonexport.csv', 'w', encoding="utf-8") as f: 
          write = csv.writer(f) 
          write.writerow(("idexport","nameexport"))
          write.writerows(export_data)
    if page == 501:
       break

