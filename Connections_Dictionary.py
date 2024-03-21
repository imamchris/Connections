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
        'category_name': 'Video games',
        'words': ['Minecraft','Roblox', 'Fortnite', 'Halo']
    }

    road_category = {
        'category_name': 'Road',
        'words': ['Traffic','Car', 'Tarmack', 'Truck']
    }

    range = [sport_category, nature_category, classroom_category, australiacities_category,
             videogames_category, road_category]

    while len(random_categories) < 4:  # Keep adding dictionaries until there are 4 in the list
        category = random.choice(range)
        if category not in random_categories:  # Check if the category is not already in the list
            random_categories.append(category)
    

    return random_categories
