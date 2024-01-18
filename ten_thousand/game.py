from ten_thousand.game_logic import GameLogic

def play(roller=GameLogic.roll_dice):
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
    print("(r)oll again, (b)ank your points or (q)uit:")
    player_choice = input("> ")
    return player_choice

if __name__ == "__main__":
    play()
