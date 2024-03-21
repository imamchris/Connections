import random
from Connections_Dictionary import selection

def get_category(): # stores/retrivies words from dictionaries 
    categories = []
    
    random_categories = selection()

    random_search = 0
    while len(categories) < 4:
        categories.append(random_categories[random_search])
        random_search += 1

    return categories



def display_category(connections): #creates the grid with a random selection of categories
    grid = [] # creates an empty list (a grid)
    row_index = 0
    
    for connection in connections:
        col_index = 0
        for word in connection ['words']: # within dictionary, get each word
            # put the word inside the correct grid reference
            grid.append(word)
            col_index = col_index + 1 # moves to next column
        row_index = row_index + 1 # moves to the next row

    random.shuffle(grid) #randomizes the order of the grid
    
    # prints the grid
    max_word_len = max(len(word) for word in grid)
    print("=" * ((10 + 3) * 4 + 1))  # Print top border of the grid
    for i in range(4):
        print('| ', end='') # prints '|' at he start of each line
        for j in range(4):
            word = (grid[i * 4 + j]) # after the following word '|' is printed
            print(f"{word.ljust(max_word_len)} | ", end= '')
        print() # move to new line
    print("=" * ((10 + 3) * 4 + 1))  # Print bottom border of the grid


def get_words():
    
    valid_guess = False

    while valid_guess == False: # keeps repeating until player guess has 4 words, and has no numbers in it 
        guess = input("What is your input? ") # Asks for an input
        word_input = guess.split()

        if guess.isdigit() == True: # checks for any integers in the players guess
            print("This input cannot have any numbers, try again...")
            valid_guess = False
        elif len(word_input) == 4: # if there are four words, valid_guess = True
            valid_guess = True
        elif len(word_input) != 4: # if it isn't four words valid_guess = False
            print("This input has to be four words at least, try again...")
            valid_guess = False
        
    
    if ',' in guess: # Removes commas from the input
        guess = guess.replace(',', ' ')

    return guess
   


def check_answer(guess, categories):  # Check if all words in the guess match any word in the categories using binary search.

    # Convert the list of dictionaries to a single list containing all words
    all_words = []
    for category in categories:
        all_words.extend(category['words'])

    guess_words = guess.split() # Split the guess into individual words

    for word in guess_words: # Perform binary search on the sorted list of words for each word in the guess
        if word not in all_words:
            print("Your answer is incorrect")
            return False

    print("Your answer is correct")
    return True



def check_win(correct_categories): # checks if all categories have been matched
    if correct_categories == 4:
        won = True
    else:
        won = False

    return won



def play_game(): # main game loop 
    categories = get_category() # sets connections to the results of the function get_category
    display_category(categories) #creates a grid
    
    lives = 4
    correct_categories = 0
    won = False

    while lives >= 0 and won == False: 
        guess = get_words() # gets the player input/guess
        answer_correct = check_answer(guess, categories) # sets answer_correct as the outcome of check_answer 
       
        if answer_correct == False:
            lives -= 1

        elif answer_correct == True:
            correct_categories += 1
            
        check_win(correct_categories)
        answer_correct = False
    
    if won == True:
        print("Congratulations you Won!")
    else:
        print(f"You lost the categories were... {categories}")

play_game() 