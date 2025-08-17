# Requirements of contacts API

## Requirements
1. Write a small, **maintainable** test suite for the **GET /contacts** endpoint.
2. The API requires authentication and exposes an auth endpoint to obtain a JWT bearer **token**.
3. Share only the source files in a **zip** file without any executables or DLLs

## Analysis
```mermaid
    sequenceDiagram
    
    Client->>Server:post(apiKey)
    Server->>Server:tokenAPI
    Server-->>Client:token

    Client->>Server:get(token)
    Server->>Server:ContactAPI
    Server-->>Client:contacts  

```

## Tasks
- [x] 1. Requirement analysis
- [x] 2. Write test plan
- [x] 3. Write test cases
- [x] 4. Postman to analyze request & response
- [x] 5. Build API automation testing framework
- [x] 6. Implement test code for token and contact API
- [x] 7. Implement integrated testing of the 2 API based on fixture
- [x] 8. Refactor project architecture to three - tier 
- [x] 9. Use schema to verify JSON format response for contact API
- [x] 10. Add edge test cases and security test cases

## Todo List
- [x] 1. Add logs and detailed exception information
- [ ] 2. Centralized management of configuration items
- [ ] 3. Read test data from yaml, csv and database
- [x] 4. Automatically send the test report after execution


## Challenges
+ AI test
+ Performance Test: Load & Stress
+ Jenkins integration
+ AOP Logger by Decorator
+ Contacts CRUD, org ,Paging
+ Determine which schema to read based on URL + CRUD + order
+ Web test by Selenium 
+ App test by Appum 
+ Screen capture, pic and video
