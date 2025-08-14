# Test cases of contacts API

## TC001 Get all contacts with valid token
* Step 1: Get the authentication token
* Step 2: Make the GET request to fetch contacts
* Step 3: Validate the response status code should be 200
* Step 4: Validate the JSON structure against the schema

## TC002 Get all contacts with invalid token
* Step 1: Get invalid token
* Step 2: Make the GET request to fetch contacts
* Step 3: Validate the response status code should be 401
* Step 4: Validate the JSON structure against the schema