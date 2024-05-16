import os

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()  # Load users when the UserManager instance is created

    def load_users(self):
        user_file_path = os.path.join('data', 'account.txt')  
        if os.path.exists(user_file_path):
            with open(user_file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(',')  
                    username = parts[0]
                    password = parts[1]
                    self.users[username] = password  # Update self.users dictionary with loaded data

    def save_user(self, username, password):
        user_folder = 'data'    
        user_file_path = os.path.join(user_folder, 'account.txt')  
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)  

        with open(user_file_path, 'a+') as file:
            file.write(f"{username},{password}\n")

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

        self.users[username] = password  # Update self.users with new user data
        print("Registration successful.")
        self.save_user(username, password)  # Save user to file
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False
