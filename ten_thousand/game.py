from ten_thousand.game_logic import GameLogic

def play(roller=GameLogic.roll_dice, num_rounds=20):
    """
    Play Ten Thousand game.

    Args:
        roller: Optional dice rolling function. Default is GameLogic.roll_dice.
        num_rounds: Optional number of rounds. Default is 20.

    Returns:
        None
    """
    total_score = 0
    round_number = 1
    quit_game = False  

    print("Welcome to Ten Thousand")
    prompt = invite_to_play()

    if prompt == "n":
        decline_game()
        return
    elif prompt == "y":
       total_score = start_game(roller, total_score, num_rounds)

def invite_to_play():
    """
    Display welcome message and prompt the user to play or decline.

    Returns:
        string "y" or "n"
    """
    print("(y)es to play or (n)o to decline")
    return input("> ")

def start_game(roller, total_score, num_rounds):
    """
    Start the game and run for the given number of rounds.

    Args:
        roller: A function to simulate rolling dice.
        total_score: The total score accumulated so far.
        num_rounds: Number of rounds to play.

    Returns:
        None
    """
    for round_number in range(1, num_rounds + 1):
        print(f"Starting round {round_number}")
        
        # Reset round_score for the new round
        round_score = 0
        
        round_score, quit_game = play_round(roller, total_score, round_number, round_score)
        if quit_game:
            break  
        total_score += round_score

def play_round(roller, total_score, round_number, round_score):
    """
    Play a round of the game.

    Args:
        roller: A function to simulate rolling dice.
        total_score: The total score accumulated so far.
        round_number: The current round number.
        round_score: The score earned in the current round.

    Returns:
        round_score: The score earned in the current round.
        quit_game: Boolean indicating if the game should be terminated.
    """
    dice_count = 6
    quit_game = False  

    while dice_count > 0:
        dice = roller(dice_count)
        print(f"Rolling {len(dice)} dice...")
        print(format_roll(dice))

        if GameLogic.calculate_score(dice) == 0:
            zilch()
            print(f"You banked 0 points in round {round_number}")
            print(f"Total score is {total_score} points")
            return round_score, False 

        player_choice = confirm_keepers(dice)
        if player_choice == ():
            print(f"Thanks for playing. You earned {total_score} points")
            return 0, True  

        invalid_choice = set(player_choice) - set(dice)
        if invalid_choice:
            print(f"Invalid choice: {invalid_choice}. Please enter valid dice.")
            continue

        dice_count -= len(player_choice)
        round_score += GameLogic.calculate_score(player_choice)

        if dice_count < 0:
            # Reset dice_count to 0 if it goes below 0
            dice_count = 0

        print(f"You have {round_score} unbanked points and {dice_count} dice remaining")
        choice = players_choice_roll_bank_quit()

        if choice == "b":
            total_score += round_score
            print(f"You banked {round_score} points in round {round_number}")
            print(f"Total score is {total_score} points")
            return round_score, False 
        elif choice == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            return 0, True  
        elif choice == "r":
            continue
    
    return round_score, False

def zilch():
    """
    Display zilch message.

    Returns:
        None
    """
    print('''
****************************************
**        Zilch!!! Round over         **
****************************************
        ''')

def confirm_keepers(roll):
    """
    Return values that the user would like to keep after being validated.

    Args:
        roll: Tuple of integers.

    Returns:
        Tuple of values to keep aka "keepers".
        An empty tuple signals a "quit".
    """

    while True:
        print("Enter dice to keep, or (q)uit:")
        keeper_string = input("> ")
        if keeper_string.lower() == 'q':
            return ()
        try:
            player_choice = convert_keepers(keeper_string, roll)
            return player_choice
        except ValueError as e:
            print(str(e))

def convert_keepers(keeper_string, roll):
    """
    Convert a given string of dice values to keep into a tuple of integers.

    Args:
        keeper_string: String input by the user.

    Returns:
        Tuple of integers.
    """
    try:
        keepers = tuple(int(char) for char in keeper_string)
    except ValueError:
        raise ValueError("Invalid input. Please enter a sequence of digits.")

    # Validate that each chosen keeper is present in the original roll
    if all(keeper in roll for keeper in keepers):
        return keepers
    else:
        raise ValueError("Invalid combination. Please enter valid dice.")

def do_roll(num_dice):
    """
    Display to the user a new roll of the given number of dice in formatted form.

    Args:
        num_dice: Number of dice to roll.

    Returns:
        Tuple representing the new roll.
    """
    return GameLogic.roll_dice(num_dice)

def format_roll(roll):
    """
    Convert the given roll into a display-friendly string.

    Args:
        roll: Tuple of integers.

    Returns:
        String representation, e.g., "*** 5 1 1 4 5 5 ***"
    """
    return f"*** {' '.join(map(str, roll))} ***"

def players_choice_roll_bank_quit():
    """
    Get the player's choice for the next action.

    Returns:
        String representing the chosen action.
    """
    print("(r)oll again, (b)ank your points or (q)uit:")
    player_choice_continue = input("> ")
    return player_choice_continue

def decline_game():
    """
    Display a message to the declining player.

    Returns:
        None
    """
    print("OK. Maybe another time")

if __name__ == "__main__":
    play()
