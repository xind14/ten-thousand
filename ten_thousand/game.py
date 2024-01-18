from ten_thousand.game_logic import GameLogic

def play(roller=GameLogic.roll_dice):
    """
    Main function to play the game of Ten Thousand.

    Parameters:
    - roller: A function to simulate rolling dice. Default is GameLogic.roll_dice.
    """
    total_score = 0
    round_number = 1
    quit_game = False  

    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    prompt = input("> ")

    if prompt == "n":
        print("OK. Maybe another time")
        return
    elif prompt == "y":
        while not quit_game: 
            print(f"Starting round {round_number}")
            round_score, total_score, quit_game = play_round(roller, total_score, round_number)
            if quit_game:
                break  
            round_number += 1

def play_round(roller, total_score, round_number):
    """
    Function to play a round of the game.

    Parameters:
    - roller: A function to simulate rolling dice.
    - total_score: The total score accumulated so far.
    - round_number: The current round number.

    Returns:
    - round_score: The score earned in the current round.
    - total_score: The updated total score.
    - quit_game: Boolean indicating if the game should be terminated.
    """
    round_score = 0
    dice_count = 6
    quit_game = False  

    while True:
        dice = roller(dice_count)
        print(f"Rolling {len(dice)} dice...")
        print(f"*** {' '.join(map(str, dice))} ***")

        player_choice = banked_dice()
        if player_choice == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            return 0, total_score, True  

        dice_count -= len(player_choice)
        round_score += GameLogic.calculate_score(player_choice)

        print(f"You have {round_score} unbanked points and {dice_count} dice remaining")
        choice = players_choice_roll_bank_quit()

        if choice == "b":
            total_score += round_score
            print(f"You banked {round_score} points in round {round_number}")
            print(f"Total score is {total_score} points")
            return round_score, total_score, False 
        elif choice == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            return 0, total_score, True  
        elif choice == "r":
            continue

def banked_dice():
    """
    Function to get the player's choice of dice to keep.

    Returns:
    - player_choice: Tuple of integers representing the chosen dice.
    """
    print("Enter dice to keep, or (q)uit:")
    player_input = input("> ")
    if player_input.lower() == 'q':
        return player_input
    try:
        player_choice = tuple(map(int, player_input))
        return player_choice
    except ValueError:
        print("Invalid input. Please enter a sequence of digits.")
        return banked_dice()

def players_choice_roll_bank_quit():
    """
    Function to get the player's choice for the next action.

    Returns:
    - player_choice: String representing the chosen action.
    """
    print("(r)oll again, (b)ank your points or (q)uit:")
    player_choice = input("> ")
    return player_choice

if __name__ == "__main__":
    play()
