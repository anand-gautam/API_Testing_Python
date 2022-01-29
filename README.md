Local API created by using json-server. Link: https://github.com/typicode/json-server . Please read the documentation on the github page. You need npm to install the json-server. Post installation, data in db is changed to as desired, and then worked on testing the APIs.

In this test, first a user record is created with POST request, grabbed the user id from it, and used it to perform rest of the actions, viz: GET, PUT, PATCH, and DELETE. After deleting again the user id is verified if it exists through GET request where 404 HTTP error status would be asserted for.

Schema validation is done using jsonschema.

Primary requirements are python 3.x version, requests library, jsonschema library. All requirements could be found in requirements.txt file
