from utils.user_manager import UserManager
from utils.dice_game import DiceGame

def main():
    print("Welcome to the Dice Roll Game!")
    
    user_manager = UserManager()
    dice_game = DiceGame()
    
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user_manager.register()
        elif choice == '2':
            user = user_manager.login()
            if user:
                dice_game.user = user
                print(f"Welcome, {user.username}!")
                while True:
                    dice_game.menu()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()