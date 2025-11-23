import hashlib

# Simple in-memory "database"
users = {}

def register(username, password):
    # Hash the password using SHA256
    hashed = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed
    print("User registered successfully!")

def login(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if users.get(username) == hashed:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Example usage
register("admin", "secure123")
login("admin", "secure123")    # ✅ Correct password
login("admin", "wrongpass")    # ❌ Incorrect password
