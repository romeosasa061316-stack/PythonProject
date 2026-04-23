Username_details = {
    "name": "Dreamer",
    "password": "123"
}

def login(username, password):
    if username == Username_details["name"] and password == Username_details["password"]:
        print("Login successful")
    else:
        print("Invalid results")

# Example usage
login("Dreamer", "123")