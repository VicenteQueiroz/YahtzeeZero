import random

class YahtzeeMechanics:
    def __init__(self):
        # Score board respectively: 1s, 2s, 3s, 4s, 5s, 6s, Set, Quads, Fullhouse, Straight, Yahtzee
        self.score_board = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.dices = [random.randint(1,6) for _ in range(5)]
        self.dices_played = 0

# Score categories
        self.action_to_score = {"1s": lambda : self.get_numbers(1), "2s": lambda : self.get_numbers(2), 
                          "3s": lambda : self.get_numbers(3), "4s": lambda : self.get_numbers(4),
                          "5s": lambda : self.get_numbers(5), "6s": lambda : self.get_numbers(6),
                          "Set": lambda : self.get_sets(3), "Quads": lambda : self.get_sets(4),
                          "Fullhouse": lambda : self.get_fullhouse(), "Straight": lambda : self.get_straight(),
                          "Yahtzee": lambda : self.get_yahtzee()}
        
        self.action_to_index = {"1s": 0, "2s": 1, "3s": 2, "4s": 3, "5s": 4, "6s": 5,
                          "Set": 6, "Quads": 7, "Fullhouse": 8, "Straight": 9, "Yahtzee": 10}

        # print(self.score_board)
        # print("\n")
        # print(self.dices)

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

    # Function that will select which score to keep from the score board
    def mark_score(self, action):
        index_to_score = self.action_to_index[action]
        # You can only mark score in a free slot
        if self.score_board[index_to_score] == -1:
            self.score_board[index_to_score] = self.action_to_score[action]()
            # If successfully managed to mark in the score board go to next turn
            self.dices_played = 0
            self.dices = [random.randint(1,6) for _ in range(5)]

            if -1 not in self.score_board:
                print("Game Over!")
                print(f"Total score: {sum(self.score_board)}")
        else:
            print(f"You already marked in {action}, try another option")

    # Function that will make the preview score for each category: [0, 0, 9, ..., 0, 50]
    def preview_score(self):
        # If successfully managed to mark in the score board go to next turn
        preview = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for index, category in enumerate(self.action_to_score.keys()):
            # Only preview unmarked categories
            if self.score_board[index] == -1:
                preview[index] = self.action_to_score[category]()
            else:
                # For the already marked/scored categories keep the same score
                preview[index] = self.score_board[index]

        return preview
    
    def get_numbers(self, number: int) -> bool:
        return self.dices.count(number) * number

    def get_sets(self, number: int) -> bool:
        """
        Returns the total number of dices for three of a kind (number = 3) and quads (number = 4)
        """
        counts = {}
        score = 0
        for x in self.dices:
            counts[x] = counts.get(x, 0) + 1
            if counts[x] >= number:
                score = sum(self.dices)
        return score

    def get_fullhouse(self) -> bool:
        """
        Returns 25 points if the roll is a Full House (3 of one number, 2 of another)
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
                        return 25
        return 0


    def get_straight(self) -> bool:
        """
        Returns 40 points if there unordered sequence 1,2,3,4,5 or 2,3,4,5,6 
        """
        if 2 in self.dices and 3 in self.dices and 4 in self.dices and 5 in self.dices:
            if 1 in self.dices or 6 in self.dices:
                return 40
        return 0
        
    def get_yahtzee(self):
        """
        Returns 50 points if there is a five of a kind regardless of dice value
        """
        counts = {}
        for x in self.dices:
            counts[x] = counts.get(x, 0) + 1
            if counts[x] == 5:
                return 50
        return 0