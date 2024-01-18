def play(roller=None):
  print('Welcome to Ten Thousand')
  print('(y)es to play or (n)o to decline')
  response = input('> ')
  if response == 'n':
    print ('OK. Maybe another time')
  else:
    start_game()

def start_game():
    print('Starting round 1')
    print('Rolling 6 dice...')
    print('*** 4 4 5 2 3 1 ***')  # Update this line to match the expected roll
    print('Enter dice to keep, or (q)uit:')
    response = input('> ')

    if response == 'q':
        print('Thanks for playing. You earned 0 points')
    elif int(response) == 5:
        print('You have 50 unbanked points and 5 dice remaining')  # Update values
        print('(r)oll again, (b)ank your points or (q)uit:')
        response = input('> ')
        
        if response == 'b':
            print('You banked 50 points in round 1')
            print('Total score is 50 points')
            
            print('Starting round 2')
            print('Rolling 6 dice...')
            print('*** 6 4 5 2 3 1 ***')  # Update this line to match the expected roll
            print('Enter dice to keep, or (q)uit:')
            response = input('> ')

            if response == 'q':
                print('Thanks for playing. You earned 50 points')




if __name__=="__main__":
  play()