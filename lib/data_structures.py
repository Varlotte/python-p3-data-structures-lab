spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    list_name = [d.get("name", "") for d in spicy_foods]
    print(list_name)
    return list_name


def get_spiciest_foods(spicy_foods):
    # Define a function get_spiciest_foods() that takes a list of spicy_foods and returns a list of dictionaries where the heat level of the food is greater than 5.
    pass


def print_spicy_foods(spicy_foods):
    # Define a function print_spicy_foods() that takes a list of spicy_foods and output to the terminal each spicy food in the following format using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
    pass


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Define a function get_spicy_food_by_cuisine() that takes a list of spicy_foods and a string representing a cuisine, and returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
    pass


def print_spiciest_foods(spicy_foods):
    # Define a function print_spiciest_foods() that takes a list of spicy_foods and outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format: Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
    pass


def get_average_heat_level(spicy_foods):
    # Define a function average_heat_level() that takes a list of spicy_foods and returns an integer representing the average heat level of all the spicy foods in the array.
    pass


def create_spicy_food(spicy_foods, spicy_food):
    # Define a function create_spicy_food() that takes a list of spicy_foods and a new spicy_food and returns the original list with the new spicy_food added.
    pass
