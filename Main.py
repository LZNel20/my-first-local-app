import random

class Player:
    def __init__(self):
        self.max_health = 35
        self.health = self.max_health
        self.inventory = {}
        
    # Inventory stuff
    def add_item(self, item_name, amount=1):
        self.inventory[item_name] = self.inventory.get(item_name, 0) + amount

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
            return
    
        print("Inventory:")
        for item, amount in self.inventory.items():
            print(f"{item}: {amount}")

    def use_item(self, item_name):
        
        print(f"Current health: {self.health}/{self.max_health}")
        if self.inventory.get(item_name, 0) <= 0:
            print("You don't have that item.")
            return

        item = ITEM_DATA.get(item_name)

        if not item:
            print("Item does nothing.")
            return

        if item["type"] == "food":
            heal_amount = item["heal"]
            self.health = min(self.max_health, self.health + heal_amount)
            self.inventory[item_name] -= 1
            print(f"You ate {item_name} and healed {heal_amount} health!")

        else:
            print("You can't use that item.")
            
    def eat_menu(self):
        while True:
            edible_items = []

            # Build list of edible items
            for item_name, amount in self.inventory.items():
                if amount > 0 and ITEM_DATA.get(item_name, {}).get("type") == "food":
                    edible_items.append(item_name)

            if not edible_items:
                print("You have no food to eat.")
                return
            
            if player.health == player.max_health:
                print("Health is full.")
                return

            print("\nFood available:")
            for item in edible_items:
                print(f"- {item} ({self.inventory[item]})")

            print("- A: Back")
            

            choice = input("What would you like to eat? ").strip()

            if choice.lower() == "a":
                return  

            found = False
            for item in edible_items:
                if item.lower() == choice.lower():
                    self.use_item(item)
                    found = True
                    break

            if not found:
                print("Invalid choice.")

player = Player()

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
    "Iron": {"type":"material"},
    "Coal": {"type":"material"},
    "Copper": {"type":"material"}}

#####################################
###          Cave Code           ###
###################################

def explore_cave():
    area = "cave"
    location = "!lost"
    while True:
        items_list = ["a rock", "a bug", "a bat", "You hear water", "iron"]
        random_item = random.choice(items_list)

        if random_item == "You hear water":
            print(random_item)
            cave_choice = input("Go toward the water? A: Follow the noise, B: Keep exploring another way ")
            if cave_choice.lower().strip() == "a":
                cave_water()
            elif cave_choice.lower().strip() == "b":
                choice(area, location)

        print(f"You found: {random_item}!")
        if random_item == "a rock":
            print("+1 rock!")
            player.add_item("Rock", 1)
            choice(area, location)
        if random_item == "a bat":
            lost_chance = random.randrange(1, 11)
            print("The bat swoops around you. ")
            if lost_chance == 1:
                lost_item = random.choice(list(player.inventory.keys()))
                print(f"The bat causes you to drop {lost_item}")
                player.inventory[lost_item] -= 1
                choice(area, location)
            else:
                print("The bat leaves flying deeper into the cave.")
                choice(area, location)
        
        if random_item == "iron":
            print("+1 iron!")
            player.add_item("Iron", 1)
            choice(area, location)
        
        else:
            choice(area, location)

def cave_water():
    area = "cave"
    location = "!lost"
    while True:
        cave_water_choice = input("You follow the noise until you come to a small stream. The water is clear and flows down deeper out of sight into the darkness. \n A: Follow the stream, B: Turn around, C: Drink some water ")
        if cave_water_choice.strip().lower() == "a":
            print("You follow the stream down deeper into the cave.")
            deep_cave()
        elif cave_water_choice.strip().lower() == "b":
            print("You turn around and head back the way you came.")
            choice(area, location)
        elif cave_water_choice.strip().lower() == "c":
            print("You bend down, cup your hands and drink some of the water. It has a metalic taste but other then that you don't notice anything wrong.")

def deep_cave():
    area = "deep cave"
    location = "!lost"
    while True:
        deep_cave_choice = input("You come to a large body of crystal clear water. The stream you were following pours into the pond rippling the water, the noise echoing off the walls. \n A: Look around, B: Turn back, " )
        event_chance = ["event", "clear"]
        random_event = random.choice(event_chance)
        if deep_cave_choice.strip().lower() == "a":
            if random_event == "event":
                print("The ground beneath you begins to shake until the floor cracks below you. Suddenly the ground gives out and you fall into the darkness.")
                dark_cave(area, location)
            elif random_event == "clear":
                items_list = ["a rock", "a bug", "copper", "coal", "iron"]
                random_item = random.choice(items_list)
                print(f"You found: {random_item}!")
                if random_item == "a rock":
                    print("+1 rock!")
                    player.add_item("Rock", 1)
                    choice(area, location)
                if random_item == "copper":
                    print("+1 copper")
                    player.add_item("Copper", 1)
                    choice(area, location)
                
                if random_item == "iron":
                    print("+1 iron!")
                    player.add_item("Iron", 1)
                    choice(area, location)
                
                if random_item == "coal":
                    print("+1 coal!")
                    player.add_item("Coal", 1)
                    choice(area, location)
                
                else:
                    choice(area, location)
            else:
                print("Error")


        elif deep_cave_choice.strip().lower() == "b":
            print("You look at the pond for a moment longer before retracing your steps back to where you were.")
            choice(area, location)

def dark_cave(area, location):
    area = "Dark Cave"
    location = "lost"
    while True:
        deep_cave_choice = input("As you land you look around, you can barly see infront of you, the only light that seems to be in the cave is from the hole you fell through. \n A: Feel around in the dark, B: Try and climb back up the hole ")
        if deep_cave_choice.strip().lower() == "a":
            print("You feel around in dark for anything.")
        if deep_cave_choice.strip().lower() == "b":
            print("You try to climb back up the hole. Unfortunately it seems to steep to climb.")

#####################################
###         Forest Code          ###
###################################

def explore_forest():
   area = "forest"
   location = "!Lost"
   while True:
        items_list = ["an apple", "a rock", "a stick", "fur", "a bug", "a deer", "a bear!", "berries"]
        random_item = random.choice(items_list)
        

        print(f"You found: {random_item}!")
        if random_item == "an apple": 
            print("+1 apple!")
            player.add_item("Apple", 1)
            choice(area, location)
        if random_item == "fur": 
            print("+1 fur!")
            player.add_item("Fur", 1)
            choice(area, location)

        if random_item == "a rock": 
           print("+1 rock!")
           player.add_item("Rock", 1)
           choice(area, location)
        if random_item == "a stick": 
            print("+1 stick!")
            player.add_item("Stick", 1)
            choice(area, location)
        if random_item == "berries": 
            print("+3 Berries!")
            player.add_item("Berry", 3)
            choice(area, location)
         
        if random_item == "a bear!":
            print("bear_encounter()")
        elif random_item == "a deer":
            deer_encounter(area, location)
        else:
            choice(area, location)

#deer encounter

def deer_encounter(area, location):
    
    battle_choice = input("Through the tree line you see a deer eating grass. Its long sprawling antlers make it seem bigger than actually is. " 
    "What would you like to do?: A: Hunt the deer B: Leave ")
    if battle_choice.lower().strip() == "a":
        damage = random.randrange(1, 21)
        print(f"You did {damage} damage!")
        if damage >= 5:
            player_choice = input("You jump from the bushes and land the hit true against the deer. The deer falls dead onto the forest floor. \n What would you like to do?: A: Harvest the deer B: Leave ")
            if player_choice.lower().strip() == "a":
                print("You take your dagger and gut the deer, taking its fur, antlers, and meat.")
                player.add_item("Fur", 3)
                print("+3 fur!")
                choice(area, location)
            elif player_choice.lower().strip() == "b":
                    print("You loook at the fallen deer, leaving it to the forest. It will make a fine meal for a pack of wolves.")
                    choice(area, location)
            else:
                print ("error")
                
        elif damage <= 4:
            print("You jump from the bushes, and strike the deer's antlers. \n The deer bucks its head making you stagger backwards allowing it to run off into the forest.")
            choice(area, location)
    elif battle_choice.lower().strip() == "b":
        print("You admire the deer a little bit longer, then, with a snap of a twig, the deer runs of into the tree line.")
        choice(area, location)

#Main Choice

def choice(area, location):
    while True:
        action = input("What would you like to do?: A: Explore, B: Eat(Not Implemented), C: Check Inventory, D: Switch Area ")

        if action.lower().strip() == "a":
            if area == "cave":
                explore_cave()
            elif area == "forest":
                explore_forest()
            elif area == "deep cave":
                deep_cave()
                
            else:
                print("Error")
        elif action.lower().strip() == "b":
            player.eat_menu()
        elif action.lower().strip() == "c":
            player.show_inventory()
        elif location != "lost":
            if action.lower().strip() == "d":
                choice_explore()
        elif action.lower().strip() == "d":
            print("You look around but are unable to find your way to another area.")

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