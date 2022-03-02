"""
This file separates all features of a player
Author: James Yoo
"""

"""
The player class to represent a trainer in pokemon
"""


class Player:
    # Class Constructor
    # Expects name (string), a list of pokemon objects, bag object, money (int), gender (Male or female), or
    # nature (string)
    def __init__(self, name, pokemon_list, bag, money, gender, nature):
        self.name = name
        self.pokemon_list = pokemon_list
        self.bag = bag
        self.money = money
        self.gender = gender
        self.nature = nature

    # Method used to return a formatted string on the information about the trainer when print is invoked
    def __str__(self):
        return f"Name: {self.name}\nMoney: {self.money}\nGender: {self.gender}\nNature: {self.nature}"


"""
The CPU class to represent a CPU in pokemon
"""


class CPU:
    # Expects a name(string), list of pokemon objects, reward_money that will be given to the player as an int,
    # gift_pokemon if applicable and given to the player when defeated, and a fact that will be printed when the
    # player has no more pokemon
    def __init__(self, name, pokemon_list, reward_money, gift_pokemon, fact):
        self.name = name
        self.pokemon_list = pokemon_list
        self.reward_money = reward_money
        self.gift_pokemon = gift_pokemon
        self.fact = fact
        self.defeated = False  # used to keep track wehether the player can challenge this CPU
