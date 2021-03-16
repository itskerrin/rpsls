import random

# Assigns choice to a number
def name_to_number(name):
  if name == 'rock':
    return 0
  elif name == 'Spock':
    return 1
  elif name == 'paper':
    return 2
  elif name == 'lizard':
    return 3
  elif name == 'scissors':
    return 4

# Finds name associated with the number
def number_to_name(number):
  if number == 0:
    return 'rock'
  elif number == 1:
    return 'Spock'
  elif number == 2:
    return 'paper'
  elif number == 3:
    return 'lizard'
  elif number == 4:
    return 'scissors'
  else:
    return 'Error. Please enter a valid choice.'

# Main function - returns winner
def rpsls(player_choice):
  choice_to_num = name_to_number(player_choice)
  print()
  print(f'You have chosen {player_choice}: {choice_to_num}')
  comp_number = random.randrange(0, 4)
  comp_num_to_choice = number_to_name(comp_number)
  print(f'Computer has chosen {comp_num_to_choice}: {comp_number}')

# Determine winner with difference % 5
  winner = (comp_number - choice_to_num) % 5
  if winner < 3:
    player_wins = False
  else:
    player_wins = True

  # Print the results
  if player_wins:
    print('Player wins!')
  elif comp_number == choice_to_num:
    print('Its a draw!')
  else:
    print('Computer wins!')