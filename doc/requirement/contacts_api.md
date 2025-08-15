# Requirements of contacts API

## Requirements
1. Write a small, maintainable test suite for the GET /contacts endpoint.
2. The API requires authentication and exposes an auth endpoint to obtain a JWT bearer token.
3. Share only the source files in a zip file without any executables or DLLs

## Tasks
- [x] 1. requirement analysis
- [x] 2. Write test plan
- [x] 3. Write test cases
- [x] 4. Debug API with Postman and analyze request and response messages
- [x] 5. Build API automation testing framework based on Python + Pytest
- [x] 6. Implement code debugging for token and contact API
- [x] 7. Implement integrated testing of the two API based on fixture
- [x] 8. Refactor the project according to a three - tier architecture
- [x] 9. Use schema to verify JSON format response for contact API
- [x] 10. Add edge test cases and security test cases

## Todo List
- [ ] 1. Add logs and detailed exception information to facilitate debugging.
- [ ] 2. Centralized management of configuration items
- [ ] 3. Read test data from yaml, csv and database
- [ ] 4. Determine which schema to read based on URL + CRUD + order
- [ ] 5. Automatically send the test report after the test is executed.
- [ ] 6. url and payload should be in a config file



## Challenges
+ AOP Logger by Decorator
+ Performance, stress test
+ Jenkins integration
+ Batch modification of parameters, batch selection of cases, batch execution
+ Paging
+ Contacts CRUD, org 