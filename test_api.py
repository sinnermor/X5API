import json

import requests
import jsonschema

class TestSuit:




    def test_base(self):
        json_schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "count": {
                    "type": "integer"
                },
                "priority": {
                    "type": "boolean"
                }
            },
            "required": [
                "name",
                "count",
                "priority"
            ]
        }
        response = requests.get('http://localhost:8080/test-api')
        response_json = json.loads(response)
        assert (response.status_code == 200)
        assert (jsonschema.validate(response_json, json_schema))


    def test_add_one(self):
        json_schema = {
          "$schema": "http://json-schema.org/draft-04/schema#",
          "type": "object",
          "properties": {
            "testId": {
              "type": "integer"
            },
            "testType": {
              "type": "string"
            },
            "log": {
              "type": "boolean"
            }
          },
          "required": [
            "testId",
            "testType",
            "log"
          ]}
        headers = {'Content-Type': 'application/json'},
        date = {"test": "auto",
                "log": True}
        response = requests.post(url='http://localhost:8080/test-api/1', json=json.dumps(date), headers=headers)
        response_json = json.loads(response)
        assert (response.status_code == 201)
        assert (jsonschema.validate(response_json, json_schema))
