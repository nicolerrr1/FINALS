import random

class DiceGame:
    def load_scores(self):
        pass

    def save_scores(self, points, stage):
        with open("Ranking.txt", "a") as f:
            f.write(f"username: points-{points}, stages-{stage}")

    def play_game(self):
        player_score = 0
        bot_score = 0
        round = 0
        total = 0
        while True:
            while bot_score < 2 and player_score < 2:
                bot_point = random.randint(1, 6)
                player_point = random.randint(1, 6)
                print(f"bot: {bot_point}")
                print(f"player: {player_point}")
                if bot_point == player_point:
                    print("It's a tie!")
                if bot_point > player_point:
                    print("You lost, Username!")
                    bot_score += 1

                if bot_point < player_point:
                    print("You won, Username!")
                    player_score += 1
                    total += 1

            if bot_score < player_score:
                print("You won the game, Username!")
                player_score += 3
                total += 3
                round += 1
                self.save_scores(total, round)
                break
            if bot_score > player_score:
                print("You lost the game, Username!")
                break

    def show_top_scores(self):
        print("Showing top scores:")
        # Load and display top scores from file

    def logout(self):
        self.user = None
        print("Logged out successfully.")

    def menu(self):
        print("Menu:")
        print("1. Start Game")
        print("2. Show Top Scores")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.play_game()
        elif choice == '2':
            self.show_top_scores()
        elif choice == '3':
            self.logout()
        else:
            print("Invalid choice. Please try again.")
