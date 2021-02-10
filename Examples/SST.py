import json
import requests

print("Öffne File..")
with open("SST.json") as json_file:
    data = json.load(json_file) #Lade den JSON job ein
print("Sende Post request..")
r = requests.post("http://localhost:80/api/v1/jobs", json=data) #Sende Job an den Server
ident = r.headers["OpenEO-Identifier"] #Kopiere Identifier
print("ID: " + ident)
print("Starte Job..")
url = "http://localhost:80/api/v1/jobs/"+ str(ident) +"/results" #Baue URL
req = requests.post(url) #Starte Job