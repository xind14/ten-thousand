from collections import Counter

import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        # Implement scoring logic based on the rules of the game
        score = 0

        # Count occurrences of each value using Counter
        counts = Counter(dice_roll)
        print("counts is:",counts)

        # Calculate score for 1s
        # score += counts[1] * (counts[1] // 3) * (100 * (counts[1] % 3))

        # Calculate score for 5s
        # score += counts[5] * (counts[5] // 3) * (50 * (counts[5] % 3))



        # Scoring for ones, twos, threes, fours, fives, sixes
        # unique_values = sorted(set(dice_roll))
        # if len(counts) == 6 and counts == [1, 2, 3, 4, 5, 6]:
        #     score += 1500
        if len(counts) == 6 and all(count == 1 for count in counts.values()):
            score += 1500
            return score


        for value in range(1,7):
            
            if value != 1 and value != 5:
                score += value * 100 * (counts[value] // 3)

            elif value == 1:
                score += 1000 * (counts[1] // 3) + 100 * (counts[1] % 3)
            elif value == 5:
                score += 500 * (counts[5] // 3) + 50 * (counts[5] % 3)

        print("dice roll count is:", dice_roll.count(value))
        print("count.items is:", counts.items())

        for value, count in counts.items():
            # if len(dice_roll) == 6 and dice_roll.count(value)==2:
            #     score += 800
            print("current score:", score)   
    
            # if count >= 4 and value != 1:
            #     score += value * 100
            #     print("current score after 4 of a kind:", score)   

            # if count >= 5 and value == 1:
            #     score += (value * 100) * (count - 4)
            #     print("current score after 5 of a kind:", score)

      
            if count >=4:
                score+= value *100
                print("current score after 4 of a kind:", score)   

            if count >=5:
                score+= value *100
                print("current score after 5 of a kind:", score)   

            if dice_roll.count(1)==6:
                score += 1800
            if dice_roll.count(1)==5:
                score += 1600
            if dice_roll.count(1)==4:
                score += 800
            if dice_roll.count(5)==4:
                score -= 50
            if dice_roll.count(5)==5:
                score -= 100
            if dice_roll.count(2)==2 and dice_roll.count(3)==2 and dice_roll.count(6)==2 :
                score += 500

          

            # if count ==6:
            #     score += value * 1000

            # if len(dice_roll) == 6 and dice_roll.count(value)==1:
            #     score += 8000
     


        # Scoring for straights
        # unique_values = sorted(set(dice_roll))
        # if len(unique_values) == 6:
        #     score +=1500
        # if len(unique_values) == 6 and unique_values == [1, 2, 3, 4, 5, 6]:
        #     score += 1500
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
