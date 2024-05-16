import random

users = {}
top_scores = []

def main_menu():
    print("\nWelcome to Dice Roll Game!")
    print("1. register")
    print("2. login")
    print("3. exit")

def game_menu(username):
    print(f"\nWelcome {username}!")
    print("1. Start a new game")
    print("2. View top-10 scores")
    print("3. Logout")

def register():
    while True:
        username = input("Enter a new username (at least 4 characters, leave blank to cancel): ")
        if username == "":
            return
        if len(username) < 4:
            print("Username must be at least 4 characters. Please try again.")
            continue
        if username in users:
            print("Username already exists. Please try again.")
            continue
        break

    while True:
        password = input("Enter a new password (at least 8 characters, leave blank to cancel): ")
        if password == "":
            return
        if len(password) < 8:
            print("Password must be at least 8 characters. Please try again.")
            continue
        break

    users[username] = password
    print("Registration successful!")

def login():
    while True:
        username = input("Enter your username (leave blank to cancel): ")
        if username == "":
            return None
        if username not in users:
            print("Username not found. Please register first.")
            continue
        break

    while True:
        password = input("Enter your password (leave blank to cancel): ")
        if password == "":
            return None
        if users[username] == password:
            print("Login successful!")
            return username
        else:
            print("Incorrect password. Please try again.")

def dice_game(username):
    points = 0
    stages_won = 0

    while True:
        print("\nStarting a new stage...")
        player_wins = 0
        computer_wins = 0
        round_number = 1

        while player_wins < 2 and computer_wins < 2:
            player_roll = random.randint(1, 6)
            computer_roll = random.randint(1, 6)
            print(f"Round {round_number}: You rolled {player_roll}, Computer rolled {computer_roll}")
            round_number += 1

            if player_roll > computer_roll:
                player_wins += 1
                points += 1
                print("You win this round!")
            elif player_roll < computer_roll:
                computer_wins += 1
                print("Computer wins this round!")
            else:
                print("It's a tie! Roll again.")

        if player_wins == 2:
            stages_won += 1
            points += 3
            print(f"Stage won! Total points: {points}, Stages won: {stages_won}")
            choice = input("Enter 1 to continue to the next stage or 0 to stop: ")
            if choice == '0':
                break
            elif choice != '1':
                print("Invalid input. Stopping the game.")
                break
        else:
            print("Game over. You didn’t win any stages.")
            break

    if stages_won > 0:
        record_score(points)

# Function to record the score in top-10 scores
def record_score(score):
    global top_scores
    if len(top_scores) < 10 or score > min(top_scores):
        top_scores.append(score)
        top_scores = sorted(top_scores, reverse=True)[:10]
        print("New high score recorded!")

# Function to view the top-10 scores
def view_top_scores():
    if top_scores:
        print("\nTop-10 Scores:")
        for idx, score in enumerate(top_scores, 1):
            print(f"{idx}. {score} points")
    else:
        print("No scores recorded yet.")

# Main application loop
def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    game_menu(username)
                    game_choice = input("Enter your choice: ")
                    if game_choice == '1':
                        dice_game(username)
                    elif game_choice == '2':
                        view_top_scores()
                    elif game_choice == '3':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function to start the application
if __name__ == "__main__":
    main()
