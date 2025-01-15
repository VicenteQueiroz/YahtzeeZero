import random
from game_mechanics import YahtzeeMechanics
from heuristicAI import HeuristicAI
import argparse

# Assuming `YahtzeeGame` and `HeuristicAI` classes are already implemented.

class YahtzeeSimulator:
    def __init__(self, num_games: int):
        self.num_games = num_games
        self.scores = []

    def simulate_game(self):
        game = YahtzeeMechanics()
        ai = HeuristicAI(game)
        
        while any(score is -1 for score in game.score_board):
            # AI plays its turn
            ai.play_turn()
        
        # Return final score (sum of all category scores)
        return sum(game.score_board)

    def run_simulations(self):
        for _ in range(self.num_games):
            final_score = self.simulate_game()
            self.scores.append(final_score)
        self.report_results()

    def report_results(self):
        avg_score = sum(self.scores) / len(self.scores)
        print(f"Simulated {self.num_games} games.")
        print(f"Average Score: {avg_score:.2f}")
        print(f"High Score: {max(self.scores)}")
        print(f"Low Score: {min(self.scores)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bot", help="Choose which bot to play") # TODO add later different arguments for different AIs
    args = parser.parse_args()
    print(args.bot)
    simulator = YahtzeeSimulator(num_games=100)
    simulator.run_simulations()
