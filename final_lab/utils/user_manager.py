import os

class UserManager:
    def __init__(self):
        self.users = {}

    def load_users(self):
        if not os.path.exists("data"):
            os.makedirs("data")

        users_file_path = os.path.join("data", "accounts.txt")
        if os.path.exists(users_file_path):
            with open(users_file_path, "r") as f:
                for line in f:
                    username, password = line.strip().split(",")
                    self.users[username] = password

    def save_users(self):
        if not os.path.exists("data"):
            os.makedirs("data")

        users_file_path = os.path.join("data", "accounts.txt")
        with open(users_file_path, "w") as f:
            for username, password in self.users.items():
                f.write(f"{username},{password}\n")

    def validate_username(self, username):
        if len(username) < 4:
            return False
        if username in self.users:
            return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            return False
        return True

    def register(self, username, password):
        if not self.validate_username(username):
            print("Invalid username. Username must be at least 4 characters long and unique.")
            return False
        if not self.validate_password(password):
            print("Invalid password. Password must be at least 8 characters long.")
            return False

        self.users[username] = password
        print("Registration successful.")
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False
