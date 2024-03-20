import random
from Connections_Dictionary import selection

def get_category(): # stores/retrivies words from dictionaries 
    categories = []

    random_categories = selection()
    print(random_categories)
    print(" ")
    
    # for i in range(1,4):
    #     categories.append(random_categories[i])
    
    
    # sport_category = {
    #     'category_name': 'Sport',
    #     'words': ['Soccer','Cricket', 'Baseball', 'Basketball']
    # }

    # nature_category = {
    #     'category_name': 'Nature',
    #     'words': ['Tree', 'Flower', 'Plant', 'Bush']
    # }

    # classroom_category = {
    #     'category_name': 'Classroom',
    #     'words': ['Whiteboard', 'Book', 'Teacher', 'Desk']
    # }

    # australiacities_category = {
    #     'category_name': 'Australian Cities',
    #     'words': ['Sydney','Melbourne', 'Darwin', 'Perth']
    # }

    # categories.append(sport_category) # Adds individual categories to categories 
    # categories.append(nature_category)
    # categories.append(classroom_category)
    # categories.append(australiacities_category)

    print(categories)

    return categories



def display_category(connections): #creates the grid with a random selection of categories
    grid = [] # creates an empty list (a grid)
    row_index = 0
    
    for connection in connections:
        col_index = 0
        for word in connection ['words']: # within dictionary, get each word
            # put the word inside the correct grid reference
            connections[row_index][col_index] = word
            grid.append(word)
            col_index = col_index + 1 # moves to next column
        row_index = row_index + 1 # moves to the next row

    random.shuffle(grid) # Randomizes the order of the grid
    print(grid) # prints the grid
 


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