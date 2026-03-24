# Section G: JSON Validation.

# You're getting JSON files, now you need to make sure that the
# information has the right schema (read: structure) and the 
# correct data types therein.

# We're going to make use of the JSONSchema library.
import json
import jsonschema
from jsonschema import validate
from pprint import pprint

# Here we create a schema, then validate some input against
# it. In the "Required" section, we list out the keys required
# in any JSON. 
transaction_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
            "InvoiceNo": {
                "type": "integer"
            },
        "StockCode": {
                "type": "integer"
                },
        "Description": {
                "type": "string"
                },
        "Quantity": {
                "type": "integer",
                },
        "InvoiceDate": {
                "type": "string"
                },
        "UnitPrice": {
                "type": "number"
                },
        "CustomerID": {
                "type": "integer"
                },
        "Country": {
                "type": "string"
                }
    },
    "required": [
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "CustomerID",
        "InvoiceDate",
        "UnitPrice"
    ]
}

# Let's try to do a simple validation of a JSON. 
# This function just returns True or False.
# We're just checking if the JSON is correct, like if
# you forgot a comma or something somewhere. We're seeing
# if the JSON.loads functions properly. Kinda useless, 
# but ok.
def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True

# Now we're just trying to validate the schema. 
# This function takes some JSON data, and sees if its
# schema matches the required schema. 
def validate_json_schema(json_data, my_schema):
    # REF: https://json-schema.org/
    schema = my_schema
    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is not valid."
        return False, err
    message = "Given JSON is valid."
    return True, message

# Main body of the Python script. Like main method in Java.
if __name__ == '__main__':

    # Open a JSON and store it in 'data' variable.
    with open("./dummy_data/data_subset.json") as json_file:
        data = json.load(json_file)

    valid_transaction_dict = data[0]
    pprint(valid_transaction_dict)  # Print out some data.

    # Try to validate the JSON to see if it's got the correct structure.
    res = validate(instance=valid_transaction_dict, schema=transaction_schema)
    print(res)
    # > None

    # Create a Dict that is missing Customer_ID.
    customer_id_missing_dict = {
        "InvoiceNo": 536370,
        "StockCode": 22492,
        "Description": "MINI PAINT SET VINTAGE",
        "Quantity": 36,
        "InvoiceDate": "12/1/2010 8:45",
        "UnitPrice": 0.65,
        "Country": "France"
    }

    # This one has an incorrect data type in its first key-value
    # pair.
    InvoiceNo_is_a_string = {
        "InvoiceNo": "536370",
        "StockCode": 22492,
        "Description": "MINI PAINT SET VINTAGE",
        "Quantity": 36,
        "InvoiceDate": "12/1/2010 8:45",
        "UnitPrice": 0.65,
        "CustomerID": 12583,
        "Country": "France",
        "CustomerID": 12583,
    }

    # Load valid JSON string.
    valid_json_string = json.dumps(valid_transaction_dict)

    # Create invalid JSON string - missing ',' delimiter.
    invalid_json_string = '{"InvoiceNo": 536370 "StockCode": 22492, "Description":  "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45",   "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}'

    # Validate a valid JSON string.
    res = validate_json(valid_json_string)
    print(res)
 
    # Validate an INVALID JSON string.
    res = validate_json(invalid_json_string)
    print(res)
 
    # Validate data with a valid schema.
    res = validate_json_schema(valid_transaction_dict,  my_schema=transaction_schema)
    print(res)

    # Validate data with an invalid schema.
    res = validate_json_schema(InvoiceNo_is_a_string,  my_schema=transaction_schema)
    print(res)