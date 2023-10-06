# Dictionary-API-flask
Dictionary API with Python and Flask
This is a simple dictionary API that takes a word as input and returns its definition as JSON output. It is built using Python and Flask.

To use the API:
Make a GET request to the /api/v1/<word> endpoint, where <word> is the word you want to look up.
For example, to look up the definition of the word "cat", you would make a request to /api/v1/cat.
The API will return a JSON object with the following keys:
word: The word you looked up.
definition: The definition of the word.
example:
request: api/v1/cat
respone: "definition": "A common four-legged animal (Felis silvestris) that is often kept as a household pet.",
