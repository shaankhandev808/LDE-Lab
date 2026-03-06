# Section F: JSON

# Previous sections were fun and play, now let's get serious.
# You're going to deal with a ton of JSON, so pay attention.
# We're going to load JSONs from file, create JSON objects from
# strings, dump JSON objects into strings, loop through JSONs, get
# specific values from JSONs, update part of a JSON, write JSON
# into a file.

# Great.

# Import the JSON module.
import json
# Import prettyprint too to break up JSON objects, which
# are usually just walls of text.
from pprint import pprint

# An example of a JSON array of objects in ./data/data_subset.json.
# [
#     {
#         "InvoiceNo": 536370,
#         "StockCode": 22492,
#         "Description": "MINI PAINT SET VINTAGE",
#         "Quantity": 36,
#         "InvoiceDate": "12/1/2010 8:45",
#         "UnitPrice": 0.65,
#         "CustomerID": 12583,
#         "Country": "France"
#     },
#     {
#         "InvoiceNo": 536372,
#         "StockCode": 22632,
#         "Description": "HAND WARMER RED POLKA DOT",
#         "Quantity": 6,
#         "InvoiceDate": "12/1/2010 9:01",
#         "UnitPrice": 1.85,
#         "CustomerID": 17850,
#         "Country": "United Kingdom"
#     },
#     ...
#     ...
# ]

# Deserialization of JSON is a conversion of JSON objects into their respective Python
# objects using a JSON decoder. It is important to note here that the json.loads()
# method will not always return a dictionary. The following table shows JSON objects
# and the Python data types after conversion.

# JSON OBJECT	PYTHON OBJECT
# object	dict
# array	        list
# string	str
# null	        None
# number(int)	int
# number(real)	float
# true	        True
# false	        False

# Load JSON from file (deserialize text or binary file containing a JSON document to a Python object)
with open("./dummy_data/data_subset.json") as json_file:
    data = json.load(json_file)
pprint(data)
# > [{'Country': 'France',
# >   'CustomerID': 12583,
# >   'Description': 'MINI PAINT SET VINTAGE',
# >   'InvoiceDate': '12/1/2010 8:45',
# >   'InvoiceNo': 536370,
# >   'Quantity': 36,
# >   'StockCode': 22492,
# >   'UnitPrice': 0.65},
# >  {'Country': 'United Kingdom',
# >   'CustomerID': 17850,
# >   'Description': 'HAND WARMER RED POLKA DOT',
# >   'InvoiceDate': '12/1/2010 9:01',
# >   'InvoiceNo': 536372,
# >   'Quantity': 6,
# >   'StockCode': 22632,
# >   'UnitPrice': 1.85},
# >  {'Country': 'Australia',
# >   'CustomerID': 12431,
# >   'Description': 'ALARM CLOCK BAKELIKE RED',
# >   'InvoiceDate': '12/1/2010 10:03',
# >   'InvoiceNo': 536389,
# >   'Quantity': 4,
# >   'StockCode': 22727,
# >   'UnitPrice': 3.75},
# >  {'Country': 'United Kingdom',
# >   'CustomerID': 14076,
# >   'Description': 'SET OF 4 PANTRY JELLY MOULDS',
# >   'InvoiceDate': '8/2/2011 15:19',
# >   'InvoiceNo': 562106,
# >   'Quantity': 1,
# >   'StockCode': 22993,
# >   'UnitPrice': 1.25}]

# Now we dump our JSON into a string.
# Deserialize object to a formatted string.
# I hate the guy that wrote these notes, he must be regarded.
# It's just one big string, not a great structure. 
json_formatted_string = json.dumps(data)
pprint(json_formatted_string)
# > ('[{"InvoiceNo": 536370, "StockCode": 22492, "Description": "MINI PAINT SET '
# >  'VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45", "UnitPrice": '
# >  '0.65, "CustomerID": 12583, "Country": "France"}, {"InvoiceNo": 536372, '
# >  '"StockCode": 22632, "Description": "HAND WARMER RED POLKA DOT", "Quantity": '
# >  '6, "InvoiceDate": "12/1/2010 9:01", "UnitPrice": 1.85, "CustomerID": 17850, '
# >  '"Country": "United Kingdom"}, {"InvoiceNo": 536389, "StockCode": 22727, '
# >  '"Description": "ALARM CLOCK BAKELIKE RED", "Quantity": 4, "InvoiceDate": '
# >  '"12/1/2010 10:03", "UnitPrice": 3.75, "CustomerID": 12431, "Country": '
# >  '"Australia"}, {"InvoiceNo": 562106, "StockCode": 22993, "Description": "SET '
# >  'OF 4 PANTRY JELLY MOULDS", "Quantity": 1, "InvoiceDate": "8/2/2011 15:19", '
# >  '"UnitPrice": 1.25, "CustomerID": 14076, "Country": "United Kingdom"}]')

# Now we convert the JSON-formatted long string to a Python object, an array that
# we can use. 
transactions_list_of_dicts = json.loads(json_formatted_string)
pprint(transactions_list_of_dicts)
# > [{'Country': 'France',
# >   'CustomerID': 12583,
# >   'Description': 'MINI PAINT SET VINTAGE',
# >   'InvoiceDate': '12/1/2010 8:45',
# >   'InvoiceNo': 536370,
# >   'Quantity': 36,
# >   'StockCode': 22492,
# >   'UnitPrice': 0.65},
# >  {'Country': 'United Kingdom',
# >   'CustomerID': 17850,
# >   'Description': 'HAND WARMER RED POLKA DOT',
# >   'InvoiceDate': '12/1/2010 9:01',
# >   'InvoiceNo': 536372,
# >   'Quantity': 6,
# >   'StockCode': 22632,
# >   'UnitPrice': 1.85},
# >  {'Country': 'Australia',
# >   'CustomerID': 12431,
# >   'Description': 'ALARM CLOCK BAKELIKE RED',
# >   'InvoiceDate': '12/1/2010 10:03',
# >   'InvoiceNo': 536389,
# >   'Quantity': 4,
# >   'StockCode': 22727,
# >   'UnitPrice': 3.75},
# >  {'Country': 'United Kingdom',
# >   'CustomerID': 14076,
# >   'Description': 'SET OF 4 PANTRY JELLY MOULDS',
# >   'InvoiceDate': '8/2/2011 15:19',
# >   'InvoiceNo': 562106,
# >   'Quantity': 1,
# >   'StockCode': 22993,
# >   'UnitPrice': 1.25}]

# So each element in this array is a dictionary object. Get the
# first element and print out its keys.
pprint(transactions_list_of_dicts[0].keys())
# > dict_keys(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])

# Loop through a list of transactions and access all 'InvoiceNo' for each transaction by using .get method with a key name 'InvoiceNo'
for transaction in transactions_list_of_dicts:
    pprint(transaction.get('InvoiceNo'))
# > 536370
# > 536372
# > 536389
# > 562106

# or more pythonic via list comprehensions:

pprint([transaction.get('InvoiceNo')
       for transaction in transactions_list_of_dicts])
# > [536370, 536372, 536389, 562106]

# Modify the object's attributes
# Update a value of the transaction with a InvoiceNo 536370

# old dictionary:
# {
#         "InvoiceNo": 536370,
#         "StockCode": 22492,
#         "Description": "MINI PAINT SET VINTAGE",
#         "Quantity": 36,
#         "InvoiceDate": "12/1/2010 8:45",
#         "UnitPrice": 0.65,
#         "CustomerID": 12583,
#         "Country": "France"
#     }

# print the dictionary with InvoiceNo 536370
for transaction in transactions_list_of_dicts:
    if transaction.get('InvoiceNo') == 536370:
        pprint(transaction)
# > {'Country': 'France',
# >  'CustomerID': 12583,
# >  'Description': 'MINI PAINT SET VINTAGE',
# >  'InvoiceDate': '12/1/2010 8:45',
# >  'InvoiceNo': 536370,
# >  'Quantity': 36,
# >  'StockCode': 22492,
# >  'UnitPrice': 0.65}


# and replace it with new dictionary

update_dict = {
    "InvoiceNo": 1,
    "StockCode": 1,
    "Description": "Updated dict",
    "Quantity": 1,
    "InvoiceDate": "9/9/9999 9:99",
    "UnitPrice": 1,
    "CustomerID": 1,
    "Country": "Nowhere"
}

for transaction in transactions_list_of_dicts:
    if transaction.get('InvoiceNo') == 536370:
        transaction.update(update_dict)
pprint(transactions_list_of_dicts)
# > [{'Country': 'Nowhere',
# >   'CustomerID': 1,
# >   'Description': 'Updated dict',
# >   'InvoiceDate': '9/9/9999 9:99',
# >   'InvoiceNo': 1,
# >   'Quantity': 1,
# >   'StockCode': 1,
# >   'UnitPrice': 1},
# >  {'Country': 'United Kingdom',
# >   'CustomerID': 17850,
# >   'Description': 'HAND WARMER RED POLKA DOT',
# >   'InvoiceDate': '12/1/2010 9:01',
# >   'InvoiceNo': 536372,
# >   'Quantity': 6,
# >   'StockCode': 22632,
# >   'UnitPrice': 1.85},
# >  {'Country': 'Australia',
# >   'CustomerID': 12431,
# >   'Description': 'ALARM CLOCK BAKELIKE RED',
# >   'InvoiceDate': '12/1/2010 10:03',
# >   'InvoiceNo': 536389,
# >   'Quantity': 4,
# >   'StockCode': 22727,
# >   'UnitPrice': 3.75},
# >  {'Country': 'United Kingdom',
# >   'CustomerID': 14076,
# >   'Description': 'SET OF 4 PANTRY JELLY MOULDS',
# >   'InvoiceDate': '8/2/2011 15:19',
# >   'InvoiceNo': 562106,
# >   'Quantity': 1,
# >   'StockCode': 22993,
# >   'UnitPrice': 1.25}]

# Converting Python objects to JSON objects is also known as serialization or JSON encoding

# Dump it back into a string:

pprint(json.dumps(transactions_list_of_dicts))
# > ('[{"InvoiceNo": 1, "StockCode": 1, "Description": "Updated dict", "Quantity": '
# >  '1, "InvoiceDate": "9/9/9999 9:99", "UnitPrice": 1, "CustomerID": 1, '
# >  '"Country": "Nowhere"}, {"InvoiceNo": 536372, "StockCode": 22632, '
# >  '"Description": "HAND WARMER RED POLKA DOT", "Quantity": 6, "InvoiceDate": '
# >  '"12/1/2010 9:01", "UnitPrice": 1.85, "CustomerID": 17850, "Country": "United '
# >  'Kingdom"}, {"InvoiceNo": 536389, "StockCode": 22727, "Description": "ALARM '
# >  'CLOCK BAKELIKE RED", "Quantity": 4, "InvoiceDate": "12/1/2010 10:03", '
# >  '"UnitPrice": 3.75, "CustomerID": 12431, "Country": "Australia"}, '
# >  '{"InvoiceNo": 562106, "StockCode": 22993, "Description": "SET OF 4 PANTRY '
# >  'JELLY MOULDS", "Quantity": 1, "InvoiceDate": "8/2/2011 15:19", "UnitPrice": '
# >  '1.25, "CustomerID": 14076, "Country": "United Kingdom"}]')

# or to a file (do not forget to specify 'w' write mode):
with open("./data/dumped_json.json", 'w') as json_file:
    json.dump(transactions_list_of_dicts, json_file)
