import random

class Weapon:
    def __init__(self, name, min_damage, max_damage, crit_chance = 0.2):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.crit_chance = crit_chance
        

    def roll_damage(self, dodging):
        if dodging == True:
            damage = random.randint(0, 3)
            return damage
        
        damage = random.randint(self.min_damage, self.max_damage)
            
        if random.random() == 0:
            print("You missed!")

        elif random.random() < self.crit_chance:
            print(" CRITICAL HIT!")
            damage *= 2

        return damage

#Ai helped fix the class
class Player:
    #Basic stuff
    def __init__(self, weapons):
        self.weapons = weapons
        self.equipped_weapon = weapons[0] if weapons else None
        self.max_health = 35
        self.health = self.max_health
        self.inventory = {}
        self.dc_visits = 1

    #Damage stuff
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
    
    def equip_weapon(self, weapon_name):
        for w in self.weapons:
            if w.name.lower() == weapon_name.lower():
                self.equipped_weapon = w
                print(f"Equipped: {self.equipped_weapon.name}")
                return
        print("Weapon not found.")
    
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
    
    def eat_menu(self, area):
        while True:
            edible_items = []

            for item_name, amount in self.inventory.items():
                if amount > 0 and ITEM_DATA.get(item_name, {}).get("type") == "food":
                    edible_items.append(item_name)

            if not edible_items:
                print("You have no food to eat.")
                return area
            
            if self.health == self.max_health:
                print("Health is full.")
                return area

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

class Mercenary:
    def __init__(self, weapons):
        self.weapons = weapons
        self.equipped_weapon = weapons[0] if weapons else None
        self.max_health = 55
        self.health = self.max_health

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
    
    def equip_weapon(self, weapon_name):
        for w in self.weapons:
            if w.name.lower() == weapon_name.lower():
                self.equipped_weapon = w
                print(f"Equipped: {self.equipped_weapon.name}")
                return
        print("Weapon not found.")
    



ITEM_DATA = {
    "Bow": {"type": "Weapon"},
    "Sword": {"type": "Weapon"},
    "Bear fur coat": {"type": "Armor"},
    "Apple": {"type": "food", "heal": 5},
    "Meat": {"type": "food", "heal": 10},
    "Berry": {"type": "food", "heal": 3},
    "Water" : {"type": "food", "heal": 2},
    "Fur": {"type": "material"},
    "Rock": {"type": "material"},
    "Stick": {"type": "material"},
    "Iron": {"type":"material"},
    "Coal": {"type":"material"},
    "Diamonds": {"type":"material"},
    "Emeralds": {"type":"material"}}

#####################################
###          Cave Code           ###
###################################

def explore_cave():
   
   
    items_list = ["a rock", "a bug", "a bat", "You hear water", "iron"]
    random_item = random.choice(items_list)

    if random_item == "You hear water":
        print(random_item)
        cave_choice = input("Go toward the water? A: Follow the noise, B: Keep exploring another way ")
        if cave_choice.lower().strip() == "a":
            return cave_water()
        elif cave_choice.lower().strip() == "b":
            return "cave"

    print(f"You found: {random_item}!")
    if random_item == "a rock":
        print("+1 rock!")
        player.add_item("Rock", 1)
        return "cave"    
    if random_item == "a bat":
        lost_chance = random.randrange(1, 11)
        print("The bat swoops around you. ")
        if lost_chance == 1:
            if player.inventory:
                lost_item = random.choice(list(player.inventory.keys()))
                print(f"The bat causes you to drop {lost_item}")
                player.inventory[lost_item] -= 1
                return "cave"
        else:
            print("The bat leaves flying deeper into the cave.")
            return "cave"
    
    if random_item == "iron":
        print("+1 iron!")
        player.add_item("Iron", 1)
        return "cave"
    
    else:
        return "cave"

def cave_water():
   
    cave_water_choice = input("You follow the noise until you come to a small stream. The water is clear and flows down deeper out of sight into the darkness. \n A: Follow the stream, B: Turn around, C: Drink some water ")
    if cave_water_choice.strip().lower() == "a":
        print("You follow the stream down deeper into the cave.")
        return deep_cave()
    elif cave_water_choice.strip().lower() == "b":
        print("You turn around and head back the way you came.")
        return "cave stream"
    elif cave_water_choice.strip().lower() == "c":
        print("You bend down, cup your hands and drink some of the water. It has a metalic taste but other then that you don't notice anything wrong.")
        return "cave stream"

def deep_cave():
   
    
    deep_cave_choice = input("You come to a large body of crystal clear water. The stream you were following pours into the pond rippling the water, the noise echoing off the walls. \n A: Look around, B: Turn back to the stream, " )
    event_chance = ["event", "clear"]
    random_event = random.choice(event_chance)
    if deep_cave_choice.strip().lower() == "a":
        if random_event == "event":
            print("The ground beneath you begins to shake until the floor cracks below you. Suddenly the ground gives out and you fall into the darkness.")
            return dark_cave()
                
        elif random_event == "clear":
            items_list = ["a rock", "a bug", "copper", "coal", "iron"]
            random_item = random.choice(items_list)
            print(f"You found: {random_item}!")
            if random_item == "a rock":
                print("+3 rock!")
                player.add_item("Rock", 3)
                return "deep cave"
            if random_item == "copper":
                print("+2 copper")
                player.add_item("Copper", 2)
                return "deep cave"
            
            if random_item == "iron":
                print("+3 iron!")
                player.add_item("Iron", 3)
                return "deep cave"
            
            if random_item == "coal":
                print("+2 coal!")
                player.add_item("Coal", 2)
                return "deep cave"
            
            else:
                return "deep cave"
        else:
            print("Error")
            return "deep cave"


    elif deep_cave_choice.strip().lower() == "b":
        print("You look at the pond for a moment longer before retracing your steps back to where you were.")
        return "cave stream"

def dark_cave():
  
    #if player.dc_visits == 1:
    
    deep_cave_choice = input("As you land you look around, you can barly see infront of you, the only light that seems to be in the cave is from the hole you fell through. \n A: Feel around in the dark, B: Try and climb back up the hole ")
    if deep_cave_choice.strip().lower() == "a":

        print("You feel around in dark for anything.")
        event_chance = ["event", "clear", "clear", "clear", "clear", "clear"]
        random_event = random.choice(event_chance)
        if random_event == "event":
            print("You find hole that you are able to climb up, returning back to the original part of the cave.")
        
            
            deep_cave()
        elif random_event == "clear":
            items_list = ["a rock", "a bug", "copper", "coal", "iron", "diamonds", "emeralds", "nothing", "The Draco Lair"]
            random_item = random.choice(items_list)
            if random_item == "a rock":
                print("+3 rock!")
                player.add_item("Rock", 3)
                return "Dark Cave"

            if random_item == "copper":
                print("+2 copper")
                player.add_item("Copper", 3)
                return "Dark Cave"
            
            if random_item == "iron":
                print("+3 iron!")
                player.add_item("Iron", 2)
                return "Dark Cave"
            
            if random_item == "coal":
                print("+2 coal!")
                player.add_item("Coal", 3)
                return "Dark Cave"
            
            if random_item == "diamonds":
                print("+1 diamonds!")
                player.add_item("Diamonds", 1)
                return "Dark Cave"
            
            if random_item == "emeralds":
                print("+1 emeralds!")
                player.add_item("Emeralds", 1)
                return "Dark Cave"

            if random_item == "nothing":
                print("You found nothing.")
                return "Dark Cave"
        
        return "Dark Cave"

    elif deep_cave_choice.strip().lower() == "b":
        print("You try to climb back up the hole. Unfortunately it seems to steep to climb.")
        return "Dark Cave"
   
                

        

#####################################
###         Forest Code          ###
###################################

def explore_forest():
   area = "forest"
   location = "!Lost"
   while True:
        items_list = ["an apple", "a rock", "a stick", "fur", "a bug", "a deer", "a bear", "berries", "a trap"]
        random_item = random.choice(items_list)
        

        print(f"You found: {random_item}!")
        if random_item == "an apple": 
            print("+1 apple!")
            player.add_item("Apple", 1)
            return "forest"
        elif random_item == "fur": 
            print("+1 fur!")
            player.add_item("Fur", 1)
            return "forest"

        elif random_item == "a rock": 
           print("+1 rock!")
           player.add_item("Rock", 1)
           return "forest"
        elif random_item == "a stick": 
            print("+1 stick!")
            player.add_item("Stick", 1)
            return "forest"
        elif random_item == "berries": 
            print("+3 Berries!")
            player.add_item("Berry", 3)
            return "forest"
         
        elif random_item == "a bear":
            bear_encounter(area, location)
        elif random_item == "a deer":
            deer_encounter(area, location)
        elif random_item == "a trap":
            trap_chance = random.randrange(1, 5)
            if trap_chance == 4:
                print("You fell into a trap! After a bit you are able to climb your way out of the trap but there seems to be someone waiting for you.")
                mercenary_encounter(area, location)
                
            else:
                print("You are able to avoid falling into the trap.")
                return "forest"
        else:
            return "forest"

#Mercenary encounter
def mercenary_encounter(area, location):
    print("The mercenary walks closer, saying, 'I know what you're doing here. You're here to kill the Draco as well!' \n Draco? This is the first you're hearing of it. You go to speak but the mercenary inturupts you. 'It doesn't matter I don't plan on sharing the gold anyway!' The mercenary draws his sword!")
    mercenary_battle(area, location)

def mercenary_battle(area, location):
    while mercenary.health > 0 and player.health > 0:
        dodging = False
        action = input("A. Attack  B. Dodge  C. Switch Weapon: ").lower().strip() 
        if action.lower().strip() == "a":
            damage = player.equipped_weapon.roll_damage(dodging)
            merc_attack = mercenary.equipped_weapon.roll_damage(dodging)
            if merc_attack == 0:
                print("The mercenary missed!")
                mercenary.health -= damage
                print(f"You did {damage} damage")
                print(f"Current health: {player.health}. Current Mercenary health: {mercenary.health}.")
            elif merc_attack >= 1:
                player.take_damage(merc_attack)
                print(f"Mercenary did {merc_attack} damage.")
                mercenary.take_damage(damage)
                print(f"You did {damage} damage")
                print(f"Current health: {player.health}. Current Mercenary health: {mercenary.health}.")
        elif action.lower().strip() == "b":
            if random.randint(1, 6) >= 4:
                dodging = True
                print("Successful dodge!")
                damage = player.equipped_weapon.roll_damage(dodging)
                mercenary.take_damage(damage)
                print(f"You did {damage} damage")
                print(f"Current health: {player.health}. Current Mercenary health: {mercenary.health}.")
            else:
                print("You failed to dodge!")
                merc_attack = mercenary.equipped_weapon.roll_damage(dodging)
                player.take_damage(merc_attack)
                print(f"The Mercenary did {merc_attack} damage!")
                print(f"Current health: {player.health}. Current Mercenary health: {mercenary.health}.")
        elif action == "c":
            for w in player.weapons:
                if w == player.equipped_weapon:
                    print(f"- {w.name} (Equipped)")
                else:
                    print(f"- {w.name}")

            new_weapon = input("Which weapon would you like to equip? ")
            player.equip_weapon(new_weapon)
        else:
            print("Error please input A, B, or C.")
    if player.health <= 0: 
        player.health = 0
        print("You died!") 
        quit()
    elif mercenary.health <= 0:
        mercenary.health = 0
        print("You defeated the Mercanary!")
        print("+2 Fur \n +3 Iron \n +1 Diamond \n +2 Apples")
        player.add_item("Fur", 2)
        player.add_item("Iron", 3)
        player.add_item("Diamonds", 1)
        player.add_item("Apple", 2)
        return "forest"
           

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
                player.add_item("Meat", 3)
                print("+3 fur!")
                print("+3 Meat!")
                choice(area, location)
            elif player_choice.lower().strip() == "b":
                    print("You loook at the fallen deer, leaving it to the forest. It will make a fine meal for a pack of wolves.")
                    choice(area, location)
            else:
                print ("error")
                
        elif damage <= 4:
            print("You jump from the bushes, and strike the deer's antlers. \n The deer bucks its head making you stagger backwards allowing it to run off into the forest.")
            return "forest"
    elif battle_choice.lower().strip() == "b":
        print("You admire the deer a little bit longer, then, with a snap of a twig, the deer runs of into the tree line.")
        return "forest"

def bear_fight(area, location):
    bear_health = 50
    while bear_health > 0 and player.health > 0:
        dodging = False
        action = input("A. Attack  B. Dodge  C. Switch Weapon: ").lower().strip() 
        if action.lower().strip() == "a":
            damage = player.equipped_weapon.roll_damage(dodging)
            bear_attack = random.randint(0, 6)
            if bear_attack == 0:
                print("The bear missed!")
                bear_health = max(0, bear_health - damage)
                print(f"You did {damage} damage")
                print(f"Current health: {player.health}. Current bear health: {bear_health}.")
            elif bear_attack >= 1:
                player.take_damage(bear_attack)
                print(f"bear did {bear_attack} damage.")
                bear_health = max(0, bear_health - damage)
                print(f"You did {damage} damage")
                print(f"Current health: {player.health}. Current bear health: {bear_health}.")
        elif action.lower().strip() == "b":
            if random.randint(1, 6) >= 4:
                dodging = True
                print("Successful dodge!")
                damage = player.equipped_weapon.roll_damage(dodging)
                bear_health = max(0, bear_health - damage)
                print(f"You did {damage} damage")
                print(f"Current health: {player.health}. Current bear health: {bear_health}.")
            else:
                print("You failed to dodge!")
                bear_attack = random.randint(3, 10)
                player.take_damage(bear_attack)
                print(f"Bear did {bear_attack} damage!")
                print(f"Current health: {player.health}. Current bear health: {bear_health}.")
        elif action == "c":
            for w in player.weapons:
                if w == player.equipped_weapon:
                    print(f"- {w.name} (Equipped)")
                else:
                    print(f"- {w.name}")

            new_weapon = input("Which weapon would you like to equip? ")
            player.equip_weapon(new_weapon)
        else:
            print("Error please input A, B, or C.")
           
    if player.health <= 0: 
        player.health = 0
        print("You died!") 
        quit()
    elif bear_health <= 0:
        bear_health = 0
        print("You defeated the bear!")
        if "Bear fur coat" not in player.inventory:
            bear_defeat(area, location)
        else:
            print("+5 Fur")
            player.add_item("Fur", 5)
            player.add_item("Meat", 6)
            choice(area, location)

                
def bear_encounter(area, location):
    while True:
        print("The bear is attacking!")
        battle_choice = input("What will you do? A: Fight. B: Run. ")
        if battle_choice.lower().strip() == "a":
            bear_fight(area, location)
        elif battle_choice.lower().strip() == "b":
            print("You attempt to run from the bear.")
            escape_number = random.choice(range(1, 7))
            print(f"You rolled a {escape_number}")
            if escape_number >= 4:
                print("You escaped the bear!")
                choice(area, location)
            else:
                print("You failed to escape the bear!")
                player.take_damage(random.randint(1, 6))
                bear_fight(area, location)
        else: 
            print("Error please pick A or B")

def bear_defeat(area, location):
    player_choice = input("The bear lays dead infront of you. What will you do to it? A: Make a fur cloak. B: Leave. ")
    if player_choice.lower().strip() == "a":
        print("You take the bear's fur and fasion it into a stunning cloak that will keep you warm at night.")
        player.max_health += 5
        player.add_item("Bear fur coat", 1)
        player.add_item("meat", 6)
        print("+Bear fur Cloak")
        print("Max Health + 5")
        print("+6 meat")
        choice(area, location)
    elif player_choice.lower().strip() == "b":
        print("You leave nature to take care of the bear's corpse.")
        return "forest"
    else:
        print("Error please choose A or B")

#Main Choice

def choice(area, location):
   while True:
        action = input("What would you like to do?: A: Explore, B: Eat, C: Check Inventory, D: Switch Area ")

        if action.lower().strip() == "a":
            if area == "cave":
                return explore_cave()
            elif area == "cave stream":
                return cave_water()
            elif area == "forest":
                return explore_forest()
            elif area == "deep cave":
                return deep_cave()
            elif area == "Dark Cave":
                return dark_cave()
                
            else:
                print("Error")
                return area
            
        elif action.lower().strip() == "b":
            player.eat_menu(area)
            continue
        elif action.lower().strip() == "c":
            player.show_inventory() 
            continue
        elif location != "lost":
            if action.lower().strip() == "d":
                return choice_explore()
        elif action.lower().strip() == "d":
            print("You look around but are unable to find your way to another area.")
        else:
            return area

def choice_explore():
    action_explore = input("Where do you want to explore? A: Forest, B: Cave ")
    if action_explore.lower() == "a":
        return "forest"
    elif action_explore.lower() == "b":
        return "cave" 
    else:
        return None

def game_start():
    area = "forest"
    location = "!lost"
    while True:
        result = choice(area, location)
        if result == "forest":
            area = "forest"
        elif result == "cave":
            area = "cave"
        elif result == "cave stream":
            area = "cave stream"
        elif result == "Dark Cave":
            area = "Dark Cave"
        elif result == "deep cave":
            area = "deep cave"
        



def Name():
    name = input("What is your Name? ")
    print(f"Hello {name}!")
    game_start()

bow = Weapon("Bow", 0, 15)
sword = Weapon("Sword", 4, 10)
mercenary = Mercenary([sword])
mercenary.equip_weapon("Sword")
player = Player([sword, bow])
player.equip_weapon("Sword")
player.add_item("Sword")
player.add_item("Bow")
Name()