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


if __name__ == "__main__":
    play()
