username = "robert"
password = "testpas123"

input_username = input("Username?")
input_password = input("Password?")

#           True                           True
if username == input_username and password == input_password:
    print(f"You are logged in {username}")
else:
    print("Invalid username or password")