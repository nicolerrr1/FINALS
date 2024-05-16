from utils import dice_game
from utils import user_manager

def main():
    dice = dice_game.DiceGame()
    user = user_manager.UserManager()

    while True:
        print("Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter your desired Username: ")
            password = input("Enter your desired Password: ")
            user.register(username,password)

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user.login(username,password)

        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()