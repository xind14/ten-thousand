from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score based on the rules of the game.

        Parameters:
        - dice_roll (tuple): A tuple representing the values rolled on dice.

        Returns:
        - calculated score.
        """
        # Implement scoring logic based on the rules of the game
        score = 0

        # Count occurrences of each value using Counter
        counts = Counter(dice_roll)
        # print("counts is:", counts)

        if len(counts) == 6 and all(count == 1 for count in counts.values()):
            score += 1500
            return score

        for value in range(1, 7):
            if value != 1 and value != 5:
                score += value * 100 * (counts[value] // 3)
            elif value == 1:
                score += 1000 * (counts[1] // 3) + 100 * (counts[1] % 3)
            elif value == 5:
                score += 500 * (counts[5] // 3) + 50 * (counts[5] % 3)

        # Check if there are exactly three values with a count of 2
        if sum(count == 2 for count in counts.values()) == 3:
    # Three pairs of any values
            score += 1500
        triple_sets = [value for value, count in counts.items() if count >= 3]
        if len(triple_sets) == 2:
            score += sum(triple_sets) * 1000 * 2

            # Subtract individual points for 1s and 5s for pairs, hot dice test now passing
            score -= min(counts[1] * 100, 300)  
            score -= min(counts[5] * 50, 150)  



        # print("dice roll count is:", counts[value])
        # print("count.items is:", counts.items())

        for value, count in counts.items():
            # print("current score:", score)
            if count >= 4:
                score += value * 100
                # print("current score after 4 of a kind:", score)

            if count >= 5:
                score += value * 100
                # print("current score after 5 of a kind:", score)

            if dice_roll.count(1) == 6:
                score += 1800
            if dice_roll.count(1) == 5:
                score += 1600
            if dice_roll.count(1) == 4:
                score += 800
            if dice_roll.count(5) == 4:
                score -= 50
            if dice_roll.count(5) == 5:
                score -= 100
            # if dice_roll.count(2) == 2 and dice_roll.count(3) == 2 and dice_roll.count(6) == 2:
            #     score += 500

        # print("current score after final:", score)

        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        Simulate rolling 'num_dice' dice.

        Parameters:
        - num_dice (int): The number of dice to roll.

        Returns:
        - tuple: A tuple representing the values rolled on the dice.
        """
        if 1 <= num_dice <= 6:
            # Generate random values for the rolled dice
            dice_values = tuple(random.randint(1, 6) for _ in range(num_dice))
            return dice_values
        else:
            raise ValueError("Number of dice should be between 1 and 6")

    @staticmethod
    def validate_keepers(roll, keepers):
        """
        Validate if the chosen keepers are legal based on the current roll.

        Parameters:
        - roll (tuple): The current roll of dice.
        - keepers (tuple): The values chosen to keep.

        Returns:
        - true if the keepers are legal, False otherwise.
        """
        # Count occurrences of each value using Counter
        roll_counts = Counter(roll)
        keepers_counts = Counter(keepers)

        # Check if the keepers are present in the current roll
        for value, count in keepers_counts.items():
            if value not in roll_counts or count > roll_counts[value]:
                return False

        return True
    
    @staticmethod
    def get_scorers(dice_roll):
        """
        Identify the scoring dice in the given roll.

        Parameters:
        - dice_roll (tuple): A tuple representing the values rolled on dice.

        Returns:
        - tuple: A tuple containing the values that contribute to the score.
        """
        # Count occurrences of each value using Counter
        counts = Counter(dice_roll)
        
        # Identify scoring dice based on the rules
        scorers = []
        for value, count in counts.items():
            if value == 1 and count >= 1:
                scorers.extend([1] * min(count, 3))
            elif value == 5 and count >= 1:
                scorers.extend([5] * min(count, 3))

        return tuple(scorers)