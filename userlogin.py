username=input("Enter your username: ")
password=input("Enter your password: ")
for i in range(3):
    if username=="admin" and password=="password123":
        print("Login successful! Welcome, admin.")
        break
    else:
        print("Login failed! Invalid username or password.")
        if i < 2:  # Allow up to 3 attempts
            username=input("Enter your username: ")
            password=input("Enter your password: ")
else:
    print("Too many failed attempts. Access denied.")
  