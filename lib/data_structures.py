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
    return [d for d in spicy_foods if d["heat_level"] > 5] or []


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        heat_level = food["heat_level"]
        print(
            f"{name} ({food['cuisine']}) | Heat Level: {'🌶'* heat_level}")


print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))
    # print(
    # f"{name} ({food['cuisine']}) | Heat Level: {'🌶'* heat_level}") if heat_level > 5 else None


def get_average_heat_level(spicy_foods):
    sum = 0
    for food in spicy_foods:
        sum = food["heat_level"] + sum

    return (sum/len(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

    # Define a function create_spicy_food() that takes a list of spicy_foods and a new spicy_food and returns the original list with the new spicy_food added.
