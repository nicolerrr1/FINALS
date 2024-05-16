import random

class DiceGame:
    def __init__(self):
        pass

    def load_scores(self):
        pass

    def save_scores(self, points, stage):
        with open("Ranking.txt", "a") as f:
            f.write(f"username: points-{points}, stages-{stage}\n")

    def play_game(self):
        player_score = 0
        bot_score = 0
        round_count = 0
        total = 0

        while True:
            while bot_score < 2 and player_score < 2:
                bot_point = random.randint(1, 6)
                player_point = random.randint(1, 6)
                print(f"bot: {bot_point}")
                print(f"player: {player_point}")
                
                if bot_point == player_point:
                    print("It's a tie!")
                elif bot_point > player_point:
                    print("You lost, !")
                    bot_score += 1
                elif bot_point < player_point:
                    print("You won, Username!")
                    player_score += 1
                    total += 1

            if bot_score < player_score:
                print("You won the game, Username!")
                player_score += 3
                total += 3
                round_count += 1
                self.save_scores(total, round_count)
                break
            elif bot_score > player_score:
                print("You lost the game, Username!")
                break

    def show_top_scores(self):
        pass

    def logout(self):
        pass

    def menu(self):
        pass

dice = DiceGame()
dice.play_game()