from utils.dice_game import DiceGame

def main():
    # Create a DiceGame instance
    dice_game = DiceGame()

    # Display the menu
    while True:
        print("Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Call register method of DiceGame
            dice_game.register()
        elif choice == '2':
            # Call login method of DiceGame
            dice_game.login()
            # If login successful, display the menu for the logged-in user
            if dice_game.current_user:
                dice_game.menu()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()