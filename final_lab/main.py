from utils import dice_game

def main():
    dice = dice_game.DiceGame()

    while True:
        print("Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
                dice_game.register()
        elif choice == '2':
            dice_game.login()
            if dice_game.current_user:
                dice_game.menu()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()