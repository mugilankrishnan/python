username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
    print("Access Granted")
else:
    print("Invalid Username or Password")
    print("Access Denied")