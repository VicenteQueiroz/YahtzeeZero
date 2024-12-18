import random

class YahtzeeMechanics:
    def __init__(self):
        # Score board respectively: 1s, 2s, 3s, 4s, 5s, 6s, Set, Quads, Fullhouse, Straight, Yahtzee
        self.score_board = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.dices = [random.randint(1,6) for _ in range(5)]
        self.dices_played = 0

        self.action_to_score = {"1": lambda : self.get_numbers(1), "2": lambda : self.get_numbers(2), 
                          "3": lambda : self.get_numbers(3), "4": lambda : self.get_numbers(4),
                          "5": lambda : self.get_numbers(5), "6": lambda : self.get_numbers(6),
                          "set": lambda : self.get_sets(3), "quads": lambda : self.get_sets(4),
                          "fullhouse": lambda : self.get_fullhouse(), "straight": lambda : self.get_straight(),
                          "yahtzee": lambda : self.get_yahtzee()}

        print(self.score_board)
        print("\n")
        print(self.dices)

    def check_state(self):
        print(self.score_board)
        print("\n")
        print(self.dices)

    def roll_dice(self, dice_to_reroll = None):
        """
        Roll dice. If no specific dice are given, roll all. [2,3] will roll the third and fourth dice
        """
        # Can only roll the dices three times
        if self.dices_played < 2:
            if dice_to_reroll is None:
                self.dices = [random.randint(1,6) for _ in range(5)]
            else:
                for i in dice_to_reroll:
                    self.dices[i] = random.randint(1, 6)
                self.dices_played += 1
            # Show to the user
            print(self.dices)

    # Function that will select which score to keep from the score board
    def mark_score(self, action):
        # If successfully managed to mark in the score board go to next turn
        if self.action_to_score[action]() == True:
            self.dices_played = 0
            self.blocked_dices = [False, False, False, False, False]
            self.dices = [random.randint(1,6) for _ in range(5)]

            if -1 in self.score_board:
                print(self.dices)
            else:
                print("Game Over!")
                print(f"Total score: {sum(self.score_board)}")

    
    def get_numbers(self, number: int) -> bool:
        if self.score_board[number - 1] == -1:
            self.score_board[number - 1] = self.dices.count(number) * number
            return True
        else:
            print(f"{number} is already marked, choose another")
            return False

    def get_sets(self, number: int) -> bool:
        """
        Adds total number of dices for three of a kind (number = 3) and quads (number = 4)
        """
        if self.score_board[number + 3] == -1:
            counts = {}
            self.score_board[number + 3] = 0
            for x in self.dices:
                counts[x] = counts.get(x, 0) + 1
                if counts[x] >= number:
                    self.score_board[number + 3] = sum(self.dices)
            return True
        else:
            print(f"Set of {number}s is already marked, choose another")
            return False

    def get_fullhouse(self) -> bool:
        """
        Adds 25 points if the roll is a Full House (3 of one number, 2 of another)
        """
        if self.score_board[8] == -1:
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
                            return True
            self.score_board[8] = 0
            return True            
        else:
            print(f"Fullhouse is already marked, choose another")
            return False


    def get_straight(self) -> bool:
        if self.score_board[9] == -1:
            self.score_board[9] = 0
            if 2 in self.dices and 3 in self.dices and 4 in self.dices and 5 in self.dices:
                if 1 in self.dices or 6 in self.dices:
                    self.score_board[9] = 40
            return True
        else:
            print(f"Straight is already marked, choose another")
            return False
        
    def get_yahtzee(self):
        if self.score_board[10] == -1:
            counts = {}
            self.score_board[10] = 0
            for x in self.dices:
                counts[x] = counts.get(x, 0) + 1
                if counts[x] == 5:
                    self.score_board[10] = 50
            return True
            

        else:
            print(f"Yahtzee is already marked, choose another")
            return False