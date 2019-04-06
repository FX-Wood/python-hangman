import random

# make a list of words to play
# words = ['buxom', 'haft', 'barbarian', 'plush', 'gambit']
words = ['boo']
# choose a word to play with
secret = words[random.randrange(len(words))]

# initialize a counter for the number of rounds
round = 0

# initialize an array for correct guesses
correct = []

# initialize an array for incorrect guesses
incorrect = []

# initialize game state
state = [
    char 
    if char in correct
    else ' _ ' 
    for char in secret
]

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

# Main game loop
while(len(correct) + len(incorrect) < 10):
    # clear window
    print('\n' * 20)
    # print a macabre hangman
    print(noose[str(round)])
    # increment round
    round += 1
    # print round
    print(f"round {round}")
    # print state
    print(f"    {' '.join(state)}   ")

    # ask user for input
    choice = input('Input a letter \n>> ')
    
    # check their answer
    if choice in secret:
        correct.append(choice)
    else:
        incorrect.append(choice)
        
    # Compute game state
    state = [
        char 
        if char in correct
        else ' _ ' 
        for char in secret
    ]

    # check win condition
    if not ' _ ' in state:
        break


# make messages for victories and losses
if not ' _ ' in state:
    # win
    print(f"    {' '.join(state)}   ")
    print(f"You got it! The word was {secret} and you guessed it in {round} attempts. \n your correct guesses: {correct} \n Your incorrect guesses: {incorrect}")
else:
    print(f"    {' '.join(state)}   ")
    print(f"You lost! Please try again. \n Your correct guesses: {correct},\n your incorrect guesses: {incorrect}")