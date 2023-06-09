import random

class DiceGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.scores = {}

    def add_player(self, name):
        self.players.append(name)
        self.scores[name] = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play(self):
        for _ in range(3):
            for player in self.players:
                roll = self.roll_dice()
                self.scores[player] += roll
                print(f"{player} rolled a {roll}")
            print()

        winner = max(self.scores, key=self.scores.get)
        print(f"{winner} wins with a total score of {self.scores[winner]}!")

def main():
    num_players = 4
    game = DiceGame(num_players)
    game.add_player("Player 1")
    game.add_player("Player 2")
    game.add_player("Player 3")
    game.add_player("Player 4")
    game.play()

if __name__ == "__main__":
    main()
