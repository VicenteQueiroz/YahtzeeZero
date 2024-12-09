import random

class Yahtzee:
    def __init__(self):
        self.score_board = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "set": 0, "quads": 0, "fullhouse": 0, "straight": 0, "yahtzee": 0}
        # Score board respectively: 1s, 2s, 3s, 4s, 5s, 6s, Set, Quads, Full house, Straight, Yahtzee
        self.score_board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.dices = [random.randint(0,6) for _ in range(5)]
        self.blocked_dices = [False, False, False, False, False]
        self.dices_played = 0

        print(self.score_board)
        print("\n")
        print(self.dices)

    def hold_dices(self, action = [False, False, False, False, False]):
        self.blocked_dices = action

    def check_state(self):
        print(self.score_board)
        print("\n")
        print(self.dices)

    def roll_dice(self):
        # Can only roll the dices three times
        if self.dices_played < 2:
            index = 0
            for blocked_dice in self.blocked_dices:
                if not blocked_dice:
                    self.dices[index] = random.randint(0,6)
                # Update number of rolled dices and the index
                index += 1
                self.dices_played += 1

    # Function that will select which score to keep from the score board
    def mark_score(self, action):
        return
    
    def get_numbers(self, number: int):
        if self.score_board[number] == 0:
            self.score_board[number] = self.dices.count(number)
        else:
            print(f"{number} is already marked, choose another")

    def get_set(self):
        counts = {}
        for x in self.dices:
            counts[x] = counts.get(x, 0) + 1
            if counts[x] >= 3:
                self.score_board[6] = sum(self.dices)

    def get_quads(self):
        counts = {}
        for x in self.dices:
            counts[x] = counts.get(x, 0) + 1
            if counts[x] >= 4:
                self.score_board[7] = sum(self.dices)

    def get_fullhouse(self):
        """
        Adds 25 points if the roll is a Full House (3 of one number, 2 of another)
        """
        # Count occurrences of each die value
        counts = {}
        for x in self.dices:
            counts[x] = counts.get(x, 0) + 1

        # Check for a Full House pattern (3+2)
        for value, count in counts.items():
            if count == 3:
                # Found 3 of a kind, check if there's another value with 2
                for other_value, other_count in counts.items():
                    if other_value != value and other_count == 2:
                        self.score_board[8] = 25

    def get_straight(self):
        if 2 in self.dices and 3 in self.dices and 4 in self.dices and 5 in self.dices:
            if 1 in self.dices or 6 in self.dices:
                self.score_board[9] = 40

    def get_yahtzee(self):
        counts = {}
        for x in self.dices:
            counts[x] = counts.get(x, 0) + 1
            if counts[x] == 5:
                self.score_board[7] = 50

game = Yahtzee()