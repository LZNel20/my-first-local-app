import random

ITEM_DATA = {
    "Bow": {"type": "Weapon"},
    "Sword": {"type": "Weapon"},
    "Apple": {"type": "food", "heal": 5},
    "Meat": {"type": "food", "heal": 10},
    "Berry": {"type": "food", "heal": 3},
    "Water" : {"type": "food", "heal": 2},
    "Fur": {"type": "material"},
    "Rock": {"type": "material"},
    "Stick": {"type": "material"},
    "Iron": {"type":"material"}}

def explore_cave():
    while True:
        items_list = ["a rock", "a bug", "a Bat", "You hear water", "iron"]
        random_item = random.choice(items_list)

        if random_item == "You hear water":
            print(random_item)
            cave_choice = input("Go toward the water? A: Follow the noise, B: Keep exploring another way ")
            if cave_choice.lower().strip() == "a":
                cave_water()
            elif cave_choice.lower().strip() == "b":
                choice_cave()

        print(f"You found: {random_item}!")
        if random_item == "a rock":
            print("+1 rock!")
        if random_item == "a Bat!":
            print("The bat swoops around you. ")
        
        if random_item == "iron":
            print("+1 iron!")
        
        else:
            choice_cave()

def cave_water():
    while True:
        cave_water_choice = input("You follow the noise until you come to a small stream. The water is clear and flows down deeper out of sight into the darkness. \n A: Follow the stream, B: Turn around C: Drink some water ")
        if cave_water_choice.strip().lower() == "a":
            print("You follow the stream down deeper into the cave.")
            deep_cave()
        elif cave_water_choice.strip().lower() == "b":
            print("You turn around and head back the way you came.")
            choice_cave()
        elif cave_water_choice.strip().lower() == "c":
            print("You bend down, cup your hands and drink some of the water. It has a metalic taste but other then that you don't notice anything wrong.")

def deep_cave():
    while True:
        deep_cave_choice = input("You come to a large body of crystal clear water. The stream you were following pours into the pond rippling the water, the noise echoing off the walls. \n A: Look around, B: Turn back," )
        if deep_cave_choice.strip().lower()
            event_chance = ["event", "clear"]
            random_event = random.choice(event_chance)
            if random.choice(random_event) == "event":
                print("The ground beneath you begins to shake until the floor cracks below you. Suddenly the ground gives out and you fall into the darkness.")
            if random.choice(random_event) == "clear":
            


def explore_forest():
    while True:
        items_list = ["an apple", "a rock", "a stick", "fur", "a bug", "a deer", "a bear!", "berries"]
        random_item = random.choice(items_list)
        print(f"You found: {random_item}!")
        if random_item == "an apple": 
            print("+1 apple!")

        if random_item == "fur": 
            print("+1 fur!")

        if random_item == "a rock": 
           print("+1 rock!")

        if random_item == "a stick": 
            print("+1 stick!")

        if random_item == "berries": 
            print("+3 Berries!")
         
        if random_item == "a bear!":
            bear_encounter()
        elif random_item == "a deer":
            deer_encounter()
        else:
            choice_forest()


            
def choice_cave():
    while True:
        action = input("What would you like to do?: A: Explore, B: Eat(Not Implemented), C: Check Inventory, D: Switch Area ")

        if action.lower().strip() == "a":
            explore_cave().strip
        elif action.lower().strip() == "b":
            player.eat_menu()
        elif action.lower().strip() == "c":
            player.show_inventory()
        elif action.lower().strip() == "d":
            choice_explore()
        else:
            print("Error")

def choice_forest():
    while True:
        action = input("What would you like to do?: A: Explore, B: Eat(Not Implemented), C: Check Inventory D: Switch Area ")

        if action.lower().strip() == "a":
            explore_forest()
        elif action.lower().strip() == "b":
            player.eat_menu()
        elif action.lower().strip() == "c":
            player.show_inventory()
        elif action.lower().strip() == "d":
            choice_explore()
        else:
            print("Error")

def choice_explore():
    action_explore = input("Where do you want to explore? A: Forest, B: Cave ")
    if action_explore.lower() == "a":
        explore_forest()
    if action_explore.lower() == "b":
        explore_cave()

def Name():
    name = input("What is your Name? ")
    print(f"Hello {name}!")
    choice_explore()

Name()