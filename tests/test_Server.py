from flask import Flask, request, jsonify
import json
import pytest
#IMPORT MUSS EVTL ANGEPASST WERDEN
from  GeoSoftII_Projekt.Server import configure_routes


@pytest.fixture(scope="module")
def app():
 app = Flask(__name__)
 return app

def test_default_route_success(app):
        configure_routes(app)
        app.testing=True
        client = app.test_client()
        url = '/'

        response = client.get(url)
        assert response.content_type == 'application/json'
        assert response.is_json == True

        assert b'api_version' in response.data
        assert b'backend_version' in response.data
        assert b'stac_version' in response.data
        assert b'WWU Projekt' in response.data
        assert b'endpoints' in response.data
        assert b'id' in response.data
        assert b'production' in response.data
        assert b'title' in response.data
        assert b'links' in response.data

        # get_json: parse data as JSON
        assert response.get_json()["api_version"] == "1.0.0"
        assert response.get_json()["backend_version"] == "1.1.2"
        assert response.get_json()["title"] == "WWU Geosoft2 Projekt"
        assert response.get_json()["description"] == "WWU Projekt"


        assert response.status_code == 200


def test_unvalid_route_failure(app):
        configure_routes(app)
        client = app.test_client()
        url = '/url_die_nicht_existiert'

        response = client.get(url)
        assert b'api_version' not in response.data
        assert b'backend_version' not in response.data
        assert b'stac_version' not in response.data
        assert b'WWU Projekt' not in response.data
        assert b'endpoints' not in response.data
        assert b'id' not in response.data
        assert b'production' not in response.data
        assert b'links' not in response.data

        assert response.is_json == False
        assert response.status_code == 404

def test_collections_success(app):

        configure_routes(app)
        client = app.test_client()
        url = '/collections'

        response = client.get(url)
        assert response.content_type == 'application/json'
        assert response.is_json == True

        # check if JSON is valid STAC collection

        '''
        assert b'stac_version'  in response.data
        assert b'id'  in response.data
        assert b'description'  in response.data
        assert b'license'  in response.data
        assert b'extent'  in response.data
        assert b'links'  in response.data
        
        assert response.get_json()["stac_version"] == "string"
        assert response.get_json()["id"] == "string"
        assert response.get_json()["description"] == "string"
        assert response.get_json()["license"] == "string"
        assert response.get_json()["extents"] == "string"
        assert response.get_json()["links"] == "string"
        
        '''





        assert response.status_code == 200


def test_collections_failure(app):
    configure_routes(app)
    client = app.test_client()
    url = '/collections'

    response = client.get(url)
    assert response.content_type == 'application/json'
    assert response.is_json == True

    # check if JSON is NOT valid STAC collection

    '''
    assert b'stac_version'  not in response.data
    assert b'id'  not in response.data
    assert b'description' not in response.data
    assert b'license' not in response.data
    assert b'extent' not in response.data
    assert b'links' not in response.data

    assert response.get_json()["stac_version"] == "string"
    assert response.get_json()["id"] == "string"
    assert response.get_json()["description"] == "string"
    assert response.get_json()["license"] == "string"
    assert response.get_json()["extents"] == "string"
    assert response.get_json()["links"] == "string"

    '''
    


    assert response.status_code == 200

def test_processes_success(app):

         configure_routes(app)
         client = app.test_client()
         url = '/processes'

         response = client.get(url)
         assert response.content_type == 'application/json'
         assert response.is_json == True
         '''
         # Test auf im Pflichtenheft festgelegtes JSON Format
         assert b'id' in response.data
         assert b'summary' in response.data
         assert b'description' in response.data
         assert b'parameter' in response.data
         
         assert response.get_json()["summary"] == "string"
         assert response.get_json()["description"] == "string"
         
         '''
         assert response.status_code == 200


def test_processes_failure(app):
    configure_routes(app)
    client = app.test_client()
    url = '/processes'

    response = client.get(url)
    assert response.content_type == 'application/json'
    assert response.is_json == True

    # Test auf das im Pflichtenheft festgelegte JSON Format
    assert b'id' not in response.data
    assert b'summary' not in response.data
    assert b'description' not in response.data
    assert b'parameter' not in response.data

    assert response.status_code == 200

def test_jobsGET_success(app):

       configure_routes(app)
       client = app.test_client()
       url = '/jobs'

       response = client.get(url)

       '''
       # Test auf im Pflichtenheft festgelegtes JSON Format
       assert b'id' in response.data
       assert b'title' in response.data
       assert b'process' in response.data
       assert b'status' in response.data
       '''
       assert response.content_type == 'application/json'
       assert response.is_json == True

       assert response.status_code ==  200


def test_jobsGET_failure(app):
    configure_routes(app)
    client = app.test_client()
    url = '/jobs'

    response = client.get(url)
    assert response.is_json == True
    assert response.content_type == 'application/json'

    # Test auf im Pflichtenheft festgelegtes JSON Format
    assert b'id' not in response.data
    assert b'title' not in response.data
    assert b'process' not in response.data
    assert b'status' not in response.data



    assert response.status_code == 200

def test_jobsPOST_success(app):
     # Todo: NOT CORRECTLY IMPLEMENTED YET
     configure_routes(app)
     client = app.test_client()
     url = '/jobs'
     '''
     mocked_request_data = {
         'id': '',
         'title': '',
         'process': '',
         'status':''
     }

     rv = client.post(url, data=json.dumps(mocked_request_data))
     json_data =rv.get_json()
     assert json_data == mocked_request_data
     assert rv.status_code ==  200
     '''

def test_jobsPOST_failure_bad_request(app):

     configure_routes(app)
     client = app.test_client()
     url = '/jobs'



     #Todo: Implementieren



     #assert response.status_code ==  400

def test_patchFromID_success(app):

      configure_routes(app)
      client = app.test_client()
      url = '/patch/<int:id>'

      # Todo: assert b'id Objekt' in response.data



#Todo: Implementieren
'''
def test_patchFromID_failure(app):
      pass

def test_deleteFromID_success(app):
     pass

def test_deleteFromID_failure(app):
    pass


def test_startFromID_success(app):
    pass

def test_startFromID_failure(app):
    pass
'''
def test_getJobFromId_success(app):
    configure_routes(app)
    client = app.test_client()
    url = '/jobs/<int:id>/results'

    response = client.get(url)
    assert response.content_type == 'application/json'
    assert response.is_json == True
    '''
    assert b'id' in response.data
    assert b'title' in response.data
    assert b'process' in response.data
    assert b'status' in response.data
    '''
    # assert response.get_json()["id"] == "string"


def test_getJobFromId_failure(app):
    configure_routes(app)
    client = app.test_client()
    url = '/jobs/<int:id>/results'

    response = client.get(url)
    assert response.content_type == 'application/json'
    assert response.is_json == True

    assert b'id' not in response.data
    assert b'title' not in response.data
    assert b'process' not in response.data
    assert b'status' not in response.data
    # assert response.get_json()["id"] != "string"
'''
def test_postData_success(app):
    pass

def test_postData_failure(app):
    pass
'''
