from flask import Flask, request, jsonify
app = Flask(__name__)

def configure_routes(app):

 @app.route("/", methods=['GET'])
 def default():
    """
    Soll ein JSON mit der Kurzübersicht unserer API Returnen
    :return: JSON
    """
    # Todo: Anpassen
    data = {"api_version": "1.0.0", "backend_version": "1.1.2", "stac_version": "string", "id": "cool-eo-cloud",
            "title": "WWU Geosoft2 Projekt", "description": "WWU Projekt", "production": False,
            "endpoints": [{"path": "/collections", "methods": ["GET"]}, {"path": "/processes", "methods": ["GET"]},
                          {"path": "/jobs", "methods": ["GET", "POST"]},
                          {"path": "/jobs/{job_id}", "methods": ["DELETE", "PATCH"]},
                          {"path": "/jobs/{job_id}/result", "methods": ["GET", "POST"]}], "links": [
            {"href": "https://www.uni-muenster.de/de/", "rel": "about", "type": "text/html",
             "title": "Homepage of the service provider"}]}

    return jsonify(data)


 @app.route("/collections", methods=['GET'])
 def collections():
    """
    Returnt alle vorhandenen Collections bei einer GET Request
    :returns:
        jsonify(data): Alle Collections in einer JSON
    """
    data = None
    return jsonify(data)


 @app.route("/processes", methods=['GET'])
 def processes():
    """
    Returnt alle vorhandenen processes bei einer GET Request
    :returns:
        jsonify(data): Alle processes in einer JSON
    """
    data = None
    return jsonify(data)

 @app.route("/jobs", methods=['GET'])
 def jobsGET():
    """
    Returnt alle vorhandenen jobs bei einer GET Request
    :returns:
        jsonify(data): Alle jobs in einer JSON
    """
    data = None
    return jsonify(data)


 @app.route("/jobs", methods=['POST'])
 def jobsPOST():
    """
    Nimmt den Body eines /jobs post request entgegen
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    dataFromPost = request.get_json()
    data = None
    return jsonify(data)

 @app.route("/patch/<int:id>", methods=['PATCH'])
 def patchFromID(id):
    """
    Nimmt den Body einer Patch request mit einer ID entgegen
    :parameter:
        id (int): Nimmt die ID aus der URL entgegen
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    dataFromPatch = request.get_json()
    data = None
    return jsonify(data)


 @app.route("/patch/<int:id>", methods=["DELETE"])
 def deleteFromID(id):
    """
    Nimmt eine Delete request für eine ID Entgegen
    :parameter:
        id (int): Nimmt die ID aus der URL entgegen
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    data = None
    return jsonify(data)


 @app.route("/jobs/<int:id>/results", methods=['POST'])
 def startFromID(id):
    """
    Startet einen Job aufgrundlage einer ID aus der URL. Nimmt ebenso den Body der Post request entgegen
    :parameter:
        id (int): Nimmt die ID aus der URL entgegen
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    dataFromPost = request.get_json()
    data = None
    return jsonify(data)


 @app.route("/jobs/<int:id>/results", methods=["GET"])
 def getJobFromID(id):
    """
    Nimmt den Body eine Patch request mit einer ID entgegen
    :parameter:
        id (int): Nimmt die ID aus der URL entgegen
    :returns:
        jsonify(data): Ergebnis des Jobs welcher mit der ID assoziiert ist.
    """
    data = None
    return jsonify(data)


 @app.route("/data", methods=["POST"])
 def postData():
    """
    Custom Route, welche nicht in der OpenEO API Vorgesehen ist. Nimmt die daten der Post request entgegen.
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    dataFromPost = request.get_json()
    data = None
    return jsonify(data)


 def main():
    """
    Startet den Server. Aktuell im Debug Modus und Reagiert auf alle eingehenden Anfragen auf Port 80.
    """
    app.run(debug=True, host="0.0.0.0", port=80)


 if __name__ == "__main__":
    main()

configure_routes(app)
