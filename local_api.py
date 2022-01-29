import requests
import jsonschema
from jsonschema import validate
import json_schema_validator

BASE_URI = "http://localhost:3000"
def post_a_user():
    global uid
    payload =   {
          "userName"  : "danish",
          "profileId" : 3,
          "id"  : 7,
          "Budget"  : 200
        }
    endpoint = "/users"
    head = {'Content-type': 'application/json','Accept': 'application/json'}
    response = requests.post(BASE_URI + endpoint, json=payload, headers=head)
    response_code = response.status_code
    print(response_code)
    response_data = response.json()
    uid = response_data['id']
    print(f"the user id created is: {uid}")
    print(response.json())
    print(response.headers['Content-Type'])
    assert response_code == 201, "Request not created"
    assert 'application/json' in response.headers['Content-Type'], "Not in Json format"

def get_created_user():
    global uid
    endpoint = f"/users/{uid}"
    response = requests.get(BASE_URI + endpoint)
    response_code = response.status_code
    print(response_code)
    response_data = response.json()
    print(response.headers['Content-Type'])
    msg = json_schema_validator.validate_json_schema('local_api_schema.json', response_data)
    print(msg)
    assert response_code == 200, "Request not fetched"
    assert 'application/json' in response.headers['Content-Type'], "Not in Json format"


def put_created_user():
    global uid
    payload = {
        "userName": "deustch",
        "profileId": 3,
        "id": 7,
        "Budget": 500
    }

    endpoint = f"/users/{uid}"
    response = requests.put(BASE_URI + endpoint, json=payload)
    response_code = response.status_code
    print(response_code)
    print(response.json())
    print(response.headers['Content-Type'])
    assert response_code == 200, "Request not put properly"
    assert 'application/json' in response.headers['Content-Type'], "Not in Json format"

def patch_created_user():
    global uid
    payload = {
        "Budget": 1000
    }
    endpoint = f"/users/{uid}"
    response = requests.put(BASE_URI + endpoint, json=payload)
    response_code = response.status_code
    print(response_code)
    print(response.json())
    print(response.headers['Content-Type'])
    assert response_code == 200, "Not patched"
    assert 'application/json' in response.headers['Content-Type'], "Not in Json format"

def delete_created_user():
    global uid
    endpoint = f"/users/{uid}"
    response = requests.delete(BASE_URI + endpoint)
    response_code = response.status_code
    print(response_code)


def verify_deleted_with_get_request():
    global uid
    endpoint = f"/users/{uid}"
    response = requests.get(BASE_URI + endpoint)
    response_code = response.status_code
    print(response_code)
    assert response_code == 404, "user still exists"


post_a_user()
get_created_user()
put_created_user()
patch_created_user()
delete_created_user()
verify_deleted_with_get_request()