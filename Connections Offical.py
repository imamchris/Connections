import random

def get_category(): # stores/retrivies words from dictionaries 
    categories = []
    
    sport_category = {
        'category_name': 'Sport',
        'words': ['Soccer','Cricket', 'Baseball', 'Basketball']
    }

    nature_category = {
        'category_name': 'Nature',
        'words': ['Tree', 'Flower', 'Plant', 'Bush']
    }

    classroom_category = {
        'category_name': 'Classroom',
        'words': ['Whiteboard', 'Book', 'Teacher', 'Desk']
    }

    australiacities_category = {
        'category_name': 'Australian Cities',
        'words': ['Sydney','Melbourne', 'Darwin', 'Perth']
    }

    categories.append(sport_category)
    categories.append(nature_category)
    categories.append(classroom_category)
    categories.append(australiacities_category)

    return categories


def display_category(): #creates the grid with a random selection of categories
    grid = []
    row_index = 0
    connections = get_category() # sets connections to the results of the function get_category

    for connection in connections:
        col_index = 0
        for word in connection ['words']: # within dictionary, get each word
            # put the word inside the correct grid reference
            connections[row_index][col_index] = word
            grid.append(word)
            col_index = col_index + 1 # moves to next column
        row_index = row_index + 1 # moves to the next row

    random.shuffle(grid)
    print(grid)

    return grid
 

def get_words():
    guess = input("What is your input? ")
    
    return guess
   

def check_answer(guess, guessed_words):

    if guess in guessed_words != True:
        print("Your answer is correct")
        answer_correct = True
        guessed_words.append(guess)
    else:
        print("Your answer is incorrect")
        answer_correct = False
        guessed_words.append(guess)
    
    print(guessed_words)
    return answer_correct
    

def play_game(): # main game loop 
    lives = 4
    correct_categories = 0
    guessed_words = []
    won = False
    display_category() #creates a grid
    while lives >= 0 and won == False: 
        guess = get_words() # gets the player input/guess
        answer_correct = check_answer(guess, guessed_words) # sets answer_correct as the outcome of check_answer 
        if answer_correct == False:
            lives -= 1
        elif answer_correct == True:
            correct_categories += 1

play_game() 