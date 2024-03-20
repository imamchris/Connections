import random

def selection():

    random_categories = []

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

    videogames_category = {
        'category_name': 'Australian Cities',
        'words': ['Minecraft','Roblox', 'Fortnite', 'Halo']
    }

    range = [sport_category, nature_category, classroom_category, australiacities_category,
             videogames_category]
    
    for i in range(1,4)
        random_category = random.choice(range)
        random_categories.append(random_category)

    return random_categories

    