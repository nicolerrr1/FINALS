import random

class DiceGame:
	def load_scores():
		pass

	def save_scores(self,points,stage):
		f = open ("Ranking.txt","a")
		f.write(f"username:  points-{points},  stages-{stage}")
		f.close()

	def play_game(self):
		player_score = 0
		bot_score = 0
		round = 0
		total = 0
		while True:
			while bot_score <2 and player_score<2:
				bot_point = random.randint(1,6)
				player_point = random.randint(1,6)
				print(f"bot: {bot_point}")
				print(f"player: {player_point}")
				if bot_point == player_point:
					print("Its a tie!")
				if bot_point > player_point:
					print("You lost, Username!")
					bot_score += 1

				if bot_point < player_point:
					print("You won, Username!")
					player_score += 1
					total +=1

			if bot_score< player_score:
				print("You won the , Username!")
				player_score+=3
				total+=3
				round+=1
				self.save_scores(total, round)
				break
			if bot_score>player_score:
				print("You lost the game, Username!")
				break
			
	def show_top_scores():
		pass

	def logout():
		pass

	def menu():
		pass

dice = DiceGame()
dice.play_game()

