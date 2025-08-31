# Test cases of everbridge web portal

## EB-LOG-001 Successful login with valid credentials
1. Navigate to login page
2. Enter valid username
3. Enter valid password
4. Click "Login"
5. Check user is redirected to the dashboard
6. Check welcome message displays correct username

## EB-LOG-002 Login failure with invalid password
1. Navigate to login page
2. Enter valid username
3. Enter incorrect password
4. Click "Login"
5. Check error message: "Invalid username or password"
5. Check user remains on login page