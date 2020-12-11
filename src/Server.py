from flask import Flask, request, jsonify

app = Flask(__name__)


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


@app.route("/.well-known/openeo", methods=["GET"])
def wellKnownEO():
    """
    Implementiert abfrage für Supported openEO Versions auf wunsch von Judith.
    Evtl. Antwort noch anpassen. Ich bin mir noch nicht ganz sicher ob das so richtig ist. Insbesondere weiß ich nicht welche version wir implementieren.

    :returns:
        jsonify(data): JSON mit der Unterstützen API Version und ein verweis auf diese.
    """
    data = {"versions": [
        {"url": "localhost/api/v1",
         "production": "false",
         "api_version": "1.0.0"}
    ]}
    return jsonify(data)


@app.route("/api/<string:version>/collections", methods=['GET'])
def collections(version):
    """
    Returnt alle vorhandenen Collections bei einer GET Request

    :returns:
        jsonify(data): Alle Collections in einer JSON
    """
    if (version == "v1"):
        data = {
            "collections": [
            ],
            "links": [
                {
                    "rel": "alternate",
                    "href": "https://example.openeo.org/csw",
                    "title": "openEO catalog (OGC Catalogue Services 3.0)"
                }
            ]
        }  # Todo: Anpassen
        return jsonify(data)
    else:
        data = {
            "id": "",  # Todo: ID Generieren bzw. Recherchieren
            "code": "404",
            "message": "Ungültiger API Aufruf.",
            "links": [
                {
                    "href": "https://example.openeo.org/docs/errors/SampleError",
                    # Todo: Passenden Link Recherchieren & Einfügen
                    "rel": "about"
                }
            ]
        }
        return jsonify(data)


@app.route("/api/<string:version>/processes", methods=['GET'])
def processes(version):
    """
    Returnt alle vorhandenen processes bei einer GET Request
    :returns:
        jsonify(data): Alle processes in einer JSON
    """
    if (version == "v1"):
        data = {
            "processes": [
            ],
            "links": [
                {
                    "rel": "alternate",
                    "href": "https://provider.com/processes",
                    "type": "text/html",
                    "title": "HTML version of the processes"
                }
            ]
        }  # Todo: Anpassen
        return jsonify(data)
    else:
        data = {
            "id": "",  # Todo: ID Generieren bzw. Recherchieren
            "code": "404",
            "message": "Ungültiger API Aufruf.",
            "links": [
                {
                    "href": "https://example.openeo.org/docs/errors/SampleError",
                    # Todo: Passenden Link Recherchieren & Einfügen
                    "rel": "about"
                }
            ]
        }
        return jsonify(data)


@app.route("/api/<string:version>/jobs", methods=['GET'])
def jobsGET(version):
    """
    Returnt alle vorhandenen jobs bei einer GET Request
    :returns:
        jsonify(data): Alle jobs in einer JSON
    """
    if (version == "v1"):
        data = {
            "jobs": [
            ],
            "links": [
                {
                    "rel": "related",
                    "href": "https://example.openeo.org",
                    "type": "text/html",
                    "title": "openEO"
                }
            ]
        }  # Todo: Anpassen
        return jsonify(data)
    else:
        data = {
            "id": "",  # Todo: ID Generieren bzw. Recherchieren
            "code": "404",
            "message": "Ungültiger API Aufruf.",
            "links": [
                {
                    "href": "https://example.openeo.org/docs/errors/SampleError",
                    # Todo: Passenden Link Recherchieren & Einfügen
                    "rel": "about"
                }
            ]
        }
        return jsonify(data)


@app.route("/api/<string:version>/jobs", methods=['POST'])
def jobsPOST(version):
    """
    Nimmt den Body eines /jobs post request entgegen
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    dataFromPost = request.get_json()
    if (version == "v1"):
        data = {"location": "URL",
                "OpenEO-Identifier": "Test"
                }  # Todo: Anpassen
        return jsonify(data)
    else:
        data = {
            "id": "",  # Todo: ID Generieren bzw. Recherchieren
            "code": "404",
            "message": "Ungültiger API Aufruf.",
            "links": [
                {
                    "href": "https://example.openeo.org/docs/errors/SampleError",
                    # Todo: Passenden Link Recherchieren & Einfügen
                    "rel": "about"
                }
            ]
        }
        return jsonify(data)


@app.route("/api/<string:version>/jobs/<int:id>", methods=['PATCH'])
def patchFromID(version, id):
    """
    Nimmt den Body einer Patch request mit einer ID entgegen
    :parameter:
        id (int): Nimmt die ID aus der URL entgegen
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    dataFromPatch = request.get_json()
    if (version == "v1"):
        data = None
        return jsonify(data)
    else:
        data = {
            "id": "",  # Todo: ID Generieren bzw. Recherchieren
            "code": "404",
            "message": "Ungültiger API Aufruf.",
            "links": [
                {
                    "href": "https://example.openeo.org/docs/errors/SampleError",
                    # Todo: Passenden Link Recherchieren & Einfügen
                    "rel": "about"
                }
            ]
        }
        return jsonify(data)


@app.route("/api/<string:version>/jobs/<int:id>", methods=["DELETE"])
def deleteFromID(version, id):
    """
    Nimmt eine Delete request für eine ID Entgegen
    :parameter:
        id (int): Nimmt die ID aus der URL entgegen
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    if (version == "v1"):
        data = None
        return jsonify(data)
    else:
        data = {
            "id": "",  # Todo: ID Generieren bzw. Recherchieren
            "code": "404",
            "message": "Ungültiger API Aufruf.",
            "links": [
                {
                    "href": "https://example.openeo.org/docs/errors/SampleError",
                    # Todo: Passenden Link Recherchieren & Einfügen
                    "rel": "about"
                }
            ]
        }
        return jsonify(data)


@app.route("/api/<string:version>/jobs/<int:id>/results", methods=['POST'])
def startFromID(version, id):
    """
    Startet einen Job aufgrundlage einer ID aus der URL. Nimmt ebenso den Body der Post request entgegen
    :parameter:
        id (int): Nimmt die ID aus der URL entgegen
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    dataFromPost = request.get_json()
    if (version == "v1"):
        data = None
        return jsonify(data)
    else:
        data = {
            "id": "",  # Todo: ID Generieren bzw. Recherchieren
            "code": "404",
            "message": "Ungültiger API Aufruf.",
            "links": [
                {
                    "href": "https://example.openeo.org/docs/errors/SampleError",
                    # Todo: Passenden Link Recherchieren & Einfügen
                    "rel": "about"
                }
            ]
        }
        return jsonify(data)


@app.route("/api/<string:version>/jobs/<int:id>/results", methods=["GET"])
def getJobFromID(version, id):
    """
    Nimmt den Body eine Patch request mit einer ID entgegen
    :parameter:
        id (int): Nimmt die ID aus der URL entgegen
    :returns:
        jsonify(data): Ergebnis des Jobs welcher mit der ID assoziiert ist.
    """
    if (version == "v1"):
        data = None
        return jsonify(data)
    else:
        data = {
            "id": "",  # Todo: ID Generieren bzw. Recherchieren
            "code": "404",
            "message": "Ungültiger API Aufruf.",
            "links": [
                {
                    "href": "https://example.openeo.org/docs/errors/SampleError",
                    # Todo: Passenden Link Recherchieren & Einfügen
                    "rel": "about"
                }
            ]
        }
        return jsonify(data)


@app.route("/data", methods=["POST"])
def postData():
    """
    Custom Route, welche nicht in der OpenEO API Vorgesehen ist. Nimmt die daten der Post request entgegen.
    :returns:
        jsonify(data): HTTP Statuscode für Erfolg (?)
    """
    dataFromPost = request.get_json()
    if (version == "v1"):
        data = None
        return jsonify(data)
    else:
        data = {
            "id": "",  # Todo: ID Generieren bzw. Recherchieren
            "code": "404",
            "message": "Ungültiger API Aufruf.",
            "links": [
                {
                    "href": "https://example.openeo.org/docs/errors/SampleError",
                    # Todo: Passenden Link Recherchieren & Einfügen
                    "rel": "about"
                }
            ]
        }
        return jsonify(data)


def main():
    """
    Startet den Server. Aktuell im Debug Modus und Reagiert auf alle eingehenden Anfragen auf Port 80.
    """
    app.run(debug=True, host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
