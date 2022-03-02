"""
This file separates all features of the bag
Author: James Yoo
"""


class Bag:
    # constructor for the bag class represented by an empty list
    def __init__(self):
        self.items = []

    # method is to add item into the bag and will expect a string of "Full Restore" or "Revive"
    def add_item(self, new_item):
        self.items.append(new_item)

    # method to use the item there will various checks for the item usage
    # For example, a pokemon with more than 1 hp will not be able to use a revive, while a pokemon with no hp can
    # not use a full restore
    def use_item(self, item_index, pokemon_list):
        # if the user opens up the bag then they will be notified that there is no items to use
        if not self.items:
            print("No items to use!")
            return
        # if there is items in teh bag the user will see their roster of pokemon to make a decision on which pokemon
        # will use the item
        print("Index, Name, Species, Health, Max Health")
        # print out the index of the pokemon as well as the pokemon's name, health, and max health
        for index, pokemon in enumerate(pokemon_list):
            print(index + 1, pokemon.name, pokemon.species, pokemon.health, pokemon.maxHp)
        # takes a user input and choose an index for the pokemon. For viewing experience the index is viewed as 1 based
        # if the user enters 0 they will escape the bag menu
        pokemon_index = int(input("Choose the pokemon to use the item on with the index number or exit with [0]: "))
        # escape the bag menu
        if pokemon_index == 0:
            return 0
        # user enters an invalid index to a pokemon
        while pokemon_index - 1 >= len(pokemon_list) or pokemon_index < 1:
            print("Index, Name, Species, Health, Max Health")
            for index, pokemon in enumerate(pokemon_list):
                print(index + 1, pokemon.name, pokemon.species, pokemon.health, pokemon.maxHp)
                print("\n")
            pokemon_index = int(input("Wrong Input, Choose the pokemon to use the item on with the index number: "))
        # store the pokemon the item will be used on as a variable
        pokemon = pokemon_list[pokemon_index - 1]
        # checks for using full restore. There are checks for fainted pokemon. For example, if a pokemon has no hp
        # the full restore can not be used if the pokemon has more than 0 hp then the full restore will set the
        # pokemon's health to full
        if self.items[item_index - 1] == "Full Restore":
            if pokemon.health == 0:
                print("Cannot use full restore on fainted pokemon\n")
                return
            elif pokemon.health == pokemon.maxHp:
                print("Cannot use full restore on non-damaged pokemon\n")
                return
            self.items.remove("Full Restore")
            return full_restore(pokemon)
        # checks for using the revive item. There are checks for when the pokemon has no fainted.
        elif self.items[item_index - 1] == "Revive":
            if pokemon.health > 0:
                print("Cannot use revive on non-fainted pokemon\n")
                return
            self.items.remove("Revive")
            return revive(pokemon)

    # method to print out all the items in the bag
    def print_contents(self):
        if not self.items:
            return "Bag is empty\n"
        for index, value in enumerate(self.items):
            print(index + 1, value)


# this is a function to emulate the above of full restore from pokemon, which will fully restore a pokemon's
# health. I implemented a feature above in the code in that fainted pokemon can not use the item
def full_restore(pokemon):
    pokemon.health = pokemon.maxHp
    return pokemon


# this is a function to represent the functionality of revive, which will expect a pokemon object and will heal the
# pokemon to half their hp if the pokemon has no hp. I implemented checks elsewhere in my code because there should be
# checks before the item is even invoked
def revive(pokemon):
    pokemon.health = pokemon.maxHp // 2
    return pokemon
