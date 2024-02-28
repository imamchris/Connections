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

    print(grid)
 

def get_words():
    guess = print(input("What is your input? "))
    
    check_answer(guess, )

    

def check_answer(guess, categories):
    guessed_words = []
    print(guessed_words)

    if guess in guessed_words != True and guess in categories:
        print("correct")
        guessed_words.append(guess)
    else:
        print("incorrect")
        guessed_words.append(guess)

    print(guessed_words)

def play_game(): # main game loop 
    display_category()
    lives = 4
    won = False
    while lives >= 0 and won == False:
        get_words()


play_game() 