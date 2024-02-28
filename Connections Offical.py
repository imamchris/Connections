def get_category(): # stores/retrivies words from dictionaries 
    categories = [0, 70, 60]

    return categories


def play_game(): # main game loop 
    display_category()
    lives = 4
    won = False
    while lives >= 0 and won == False:
        get_words()

def display_category(): #creates the grid with a random selection of categories
    # grid = []
    # row_index = 0

    # for connection in categories:
    #     col_index = 0
    #     for word in connection: # ['words']: # within dictionary, get each word
    #         # put the word inside the correct grid reference
    #         categories[row_index][col_index] = word
    #         grid.append(word)
    #         col_index = col_index + 1 # moves to next column
    #     row_index = row_index + 1 # moves to the next row

    # print(grid)

    


def get_words():
    guess = print(input("What is your input? "))
    return guess
    


def check_answer():
    print("Check Answers")


play_game() 