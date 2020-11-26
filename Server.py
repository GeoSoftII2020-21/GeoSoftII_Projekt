from flask import Flask, request, jsonify, json


app = Flask(__name__)

#Get Request für die Kurzübersicht über die API
@app.route("/", methods=['GET'])
def default():
    """
    Soll ein JSON mit der Kurzübersicht unserer API Returnen
    :return: JSON
    """
    # Entnommen aus der OpenEO API
    #Todo: Anpassen
    #API Übersicht
    data = { "api_version": "1.0.0", "backend_version": "1.1.2", "stac_version": "string", "id": "cool-eo-cloud", "title": "WWU Geosoft2 Projekt", "description": "WWU Projekt", "production": False, "endpoints": [ { "path": "/collections", "methods": [ "GET" ] }, { "path": "/processes", "methods": [ "GET" ] }, { "path": "/jobs", "methods": [ "GET", "POST" ] }, { "path": "/jobs/{job_id}", "methods": [ "DELETE", "PATCH" ] }, { "path": "/jobs/{job_id}/result", "methods": [ "GET", "POST" ] } ], "links": [ { "href": "https://www.uni-muenster.de/de/", "rel": "about", "type": "text/html", "title": "Homepage of the service provider" } ] }
    return jsonify(data)

#Gibt die Collections aus bei Get Request
@app.route("/collections", methods=['GET'])
def collections():
    """
    Return alle vorhandenen Collections bei einer GET Request
    :rtype: object
    """
    #Docstring

    #Collections müssten Abgefragt werden
    data = None
    return jsonify(collections)

#Gibt die Processes aus bei Get Request
@app.route("/processes", methods=['GET'])
def processes():
    """
    Return die Processes
    :return: Processes
    """
    #Processes müssten Abgefragt werden
    data = None
    return jsonify(processes)

#Get Reuqest für Jobs
@app.route("/jobs", methods=['GET'])
def jobsGET():
    """
    Return die Jobs
    :return: Jobs
    """
    data = None
    return jsonify(data)

#Post Request für Jobs
@app.route("/jobs", methods=['POST'])
def jobsPOST():
    """
    Nimmt den Body eines /jobs post request entgegen
    :return:
    """
    dataFromPost = request.get_json()
    data = None
    return jsonify(data)

#Patch  Request. Id ist erstmal als int angegeben. Andere Datentypen wie String UUID auch nutzbar
@app.route("/patch/<int:id>",methods=['PATCH'])
def patchFromID(id):
    """
    Nimmt den Body eine Patch request mit einer ID entgegen
    :param id:
    :return:
    """
    dataFromPatch = request.get_json()
    data = None
    return jsonify(data)

#Nimmt eine Delete Request entgegen
@app.route("/patch/<int:id>",methods=["DELETE"])
def deleteFromID(id):
    """
    Nimmt eine Delete Request entgegen
    :param id:
    :return:
    """
    data = None
    return jsonify(data)

#Post methode zum Job Starten. Nimmt JSON Body entgegen und erwartet ID
@app.route("/jobs/<int:id>/results",methods=['POST'])
def startFromID(id):
    """
    Post methode zum Job Starten. Nimmt JSON Body entgegen und erwartet ID
    :param id:
    :return:
    """
    dataFromPost = request.get_json()
    data = None
    return jsonify(data)

#Gibt die Ergebnisse eines Jobs aus
@app.route("/jobs/<int:id>/results",methods=["GET"])
def getJobFromID(id):
    """
    Gibt die Ergebnisse eines Jobs aus
    :param id:
    :return:
    """
    data = None
    return jsonify(data)

#Lässt dateien Upload zu
@app.route("/data",methods=["POST"])
def postData():
    """
    Lässt dateien Upload zu
    :return:
    """
    dataFromPost = request.get_json()
    data = None
    return data

# Startet den Job
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)