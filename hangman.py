import random

# make a list of words to play
words = ['buxom', 'haft', 'barbarian', 'plush', 'gambit']

# choose a word to play with
secret = words[random.randrange(len(words))]

# initialize a counter for the number of guesses
round = 0


# initialize an array for correct guesses
correct = []

# initialize an array for incorrect guesses
incorrect = []

# initialize an array to hold the order of the guesses

# make messages for victories and losses
win = f"You got it! The word was {secret} and you guessed it in {round} rounds. \n Your incorrect guesses: {incorrect}"
lose = f"You lost! Please try again. \n Your correct guesses: {correct},\n your incorrect guesses: {incorrect}"

# Welcome user to the game
print('\n'* 20)
print(f"Welcome to Hangman \n\n\n  'play for your life'")
print('         - the executioner\n\n')
print('\n' * 4)
input('press enter to continue...\n>> ')
print('\n' * 20)
print(f"Your secret word has {len(secret)} letters\n\n")


# make art assets
noose = {}
noose["0"] = """
    
   
    
    
    
 _____
|     |

"""
noose["1"] = """
    _____
   |   
   |   
   |   
   |  
 __|__ 
|     |

"""

noose["2"] = """
    _____
   |     |
   |   
   |  
   |  
 __|__
|     |

"""

noose["3"] = """
    _____
   |     |
   |     O
   |  
   |  
 __|__
|     |

"""

noose["4"] = """
    _____
   |     |
   |     O
   |     |
   |  
 __|__
|     |

"""
noose["5"] = """
    _____
   |     |
   |     O
   |   \_|
   |    
 __|__
|     |

"""
noose["6"] = """
    _____
   |     |
   |     O
   |   \_|_/
   |    
 __|__ 
|     |

"""
noose["7"] = """
    _____
   |     |
   |     O
   |   \_|_/
   |     |
 __|__  
|     |

"""

noose["8"] = """
    _____
   |     |
   |     O
   |   \_|_/
   |     |
 __|__  /
|     |

"""

noose["9"] = """
    _____
   |     |
   |     O
   |   \_|_/
   |     |
 __|__  / \\
|     |

"""

# main game loop
while(len(correct) + len(incorrect) < 10):
    print('\n' * 20)
    # print a macabre hangman
    print(noose[str(round)])
    # increment the attempt counter
    round += 1
    # at the beginning of each round, give game state
    # round
    print(f"round {round}")
    # make a state comprehension
    state = [
        char 
        if char in correct
        else ' _ ' 
        for char in secret
    ]

    print(f"    {' '.join(state)}   ")

    # ask user for input
    choice = input('Input a letter \n>> ')
    
    # check their answer
    if choice in secret:
        correct.append(choice)
    else:
        incorrect.append(choice)
        
    
    # check win condition
    if len(correct) == len(secret):
        break

    # print game state
    print('')


# make messages for victories and losses
if (len(correct) == len(secret)):
    # win
    print(f"You got it! The word was {secret} and you guessed it in {round} attempts. \n your correct guesses: {correct} \n Your incorrect guesses: {incorrect}")
else:
    print(f"You lost! Please try again. \n Your correct guesses: {correct},\n your incorrect guesses: {incorrect}")