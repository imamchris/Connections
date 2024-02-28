def get_category():
    print("get_category")


def play_game():
    lives = 4
    won = False
    display_category()
    while lives >= 0 and won == False:
        get_words()


def display_category():
    print("grid")


def get_words():
    guess = print(input("What is your input? "))

    if guess == True:
        print("Yay")


play_game() 