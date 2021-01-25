import os
import json
import requests
import time
import subprocess
import docker

client = docker.from_env()

print("Startup")
print("Downloade und Erstelle Dockerfile")
x = requests.get("https://raw.githubusercontent.com/GeoSoftII2020-21/GeoSoftII_Projekt/Docker-compose/docker-compose.yml") #Downloade docker Compose File
time.sleep(5)
with open("docker-compose.yml","w+") as text_file:
    text_file.write(x.text) #Schreibe docker Compose File auf festplatte
time.sleep(5)
print("Starte Docker...")
print("Downloade Images...")
client.images.pull("felixgi1516/geosoft2_dataserver")
client.images.pull("felixgi1516/geosoft2_jobmanagement")
client.images.pull("felixgi1516/geosoft2_frontend")
client.images.pull("felixgi1516/geosoft2_sst_process")
client.images.pull("felixgi1516/geosoft2_ndvi_process")
print("Image Downloads Fertig..")
child = subprocess.Popen("docker-compose up",shell=True) # Starte das Docker Compose File
time.sleep(15)
with open("job.json") as json_file:
    data = json.load(json_file) #Lade den JSON job ein
print("Sende Job Post Request")
r = requests.post("http://localhost:8080/api/v1/jobs", json=data) #Sende Job an den Server
time.sleep(5)
ident = r.headers["OpenEO-Identifier"] #Kopiere Identifier
print("Starte Job")
url = "http://localhost:8080/api/v1/jobs/"+ str(ident) +"/results" #Baue URL
req = requests.post(url) #Starte Job
print("Warte bis Job Fertig ist..")
while True:

    status = requests.get("http://localhost:8080/api/v1/jobs") #Checken wie der Job Status ist
    status = status.json()
    if status["jobs"][0]["status"] == "error": #Job gescheitert, was unser problem ist
        print("Job Gescheitert. Siehe Docker Compose Log!")
        break
    if status["jobs"][0]["status"] == "done": #Job erfolgreich.
        print("Job Erfolgreich. Siehe Docker Compose Log!")
        break
    print("Job noch nicht Fertig..")
    time.sleep(5) #Warte um server nicht zu überlasten
print("Job Fertig!")