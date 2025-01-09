from game_mechanics import YahtzeeMechanics

# Score categories
CATEGORIES = ["1s", "2s", "3s", "4s", "5s", "6s", "Set", "Quads", "Fullhouse", "Straight", "Yahtzee"]

class HeuristicAI:
    """Basic AI class for Yahtzee decisions."""
    def __init__(self, game: YahtzeeMechanics):
        self.game = game

    def choose_dice_to_reroll(self) -> list:
        """Select dice to reroll based on a simple heuristic."""
        # Example heuristic: Keep dice that are part of the highest frequency
        dice_count = {value: self.game.dices.count(value) for value in range(1, 7)}
        target_value = max(dice_count, key=dice_count.get)  # Most common value
        return [i for i, value in enumerate(self.game.dices) if value != target_value]

    def choose_category(self) -> str:
        """Select the best scoring category based on the current dice."""
        # Example heuristic: Choose the first available category
        for index, value in enumerate(self.game.score_board):
            if value is -1:
                return CATEGORIES[index]
        return None  # No available category

    def play_turn(self):
        """Play a full turn using the AI."""
        while self.game.dices_played < 2:
            dice_to_reroll = self.choose_dice_to_reroll()
            self.game.roll_dice(dice_to_reroll)
        category = self.choose_category()
        if category:
            self.game.mark_score(category)