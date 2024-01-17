from collections import Counter

import random
class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        # Implement scoring logic based on the rules of the game
        score = 0

        # Count occurrences of each value using Counter
        counts = Counter(dice_roll)
        print("counts is:", counts)

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

        print("dice roll count is:", dice_roll.count(value))
        print("count.items is:", counts.items())

        for value, count in counts.items():
            print("current score:", score)
            if count >= 4:
                score += value * 100
                print("current score after 4 of a kind:", score)

            if count >= 5:
                score += value * 100
                print("current score after 5 of a kind:", score)

        # Special cases using the more concise version
        for count in [6, 5, 4]:
            if counts[1] == count:
                score += 2000 if count == 6 else 1000 * (count - 3)

        if counts[5] == 4:
            score -= 50

        if counts[5] == 5:
            score -= 100

        if all(counts[val] == 2 for val in [2, 3, 6]):
            score += 500

        print("current score after final:", score)

        return score

    @staticmethod
    def roll_dice(num_dice):
        # Simulate rolling 'num_dice' dice
        if 1 <= num_dice <= 6:
            # Generate random values for the rolled dice
            dice_values = tuple(random.randint(1, 6) for _ in range(num_dice))
            return dice_values
        else:
            raise ValueError("Number of dice should be between 1 and 6")
