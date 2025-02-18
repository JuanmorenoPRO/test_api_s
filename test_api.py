import requests
import pytest
from jsonschema import validate

EXPECTED_SCHEMA = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "number"
      },
      "name": {
        "type": "string"
      },
      "address": {
        "type": "string"
      },
      "zip": {
        "type": "string"
      },
      "country": {
        "type": "string"
      },
      "employeeCount": {
        "type": "number"
      },
      "industry": {
        "type": "string"
      },
      "marketCap": {
        "type": "number"
      },
      "domain": {
        "type": "string"
      },
      "logo": {
        "type": "string"
      },
      "ceoName": {
        "type": "string"
      }
    },
    "required": [
      "id",
      "name",
      "address",
      "zip",
      "country",
      "employeeCount",
      "industry",
      "marketCap",
      "domain",
      "logo",
      "ceoName"
    ]
  }
}

URL = "https://fake-json-api.mock.beeceptor.com/companies"

@pytest.mark.api_test
def test_get_companies():
    response = requests.get(URL)
    assert response.status_code == 200, f"Expected code: {response.status_code}"
    
    json_data = response.json()
    validate(instance=json_data, schema=EXPECTED_SCHEMA)
