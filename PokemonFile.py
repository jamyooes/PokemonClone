"""
This file separates all features of a pokemon
Author: James Yoo
"""

"""
Pokemon class to represent a pokemon
Methods:
        damaged- this method will deduct the health of the pokemon
        print_mon- this method will print out all the information related to the pokemon
        print_moves- this method will print out all the moves and power to the current pokemon
"""
class Pokemon:
    # Class constructor
    #Expects the name of the pokemon, species of the pokemon, type of pokemon, nature of the pokemon, list of moves
    # objects, health, and gender of the pokemon
    def __init__(self, name, species, type_of_pokemon, nature, moves, health, gender):
        self.name = name
        self.species = species
        self.health = health
        self.moves = moves
        self.type_of_pokemon = type_of_pokemon
        self.nature = nature
        self.gender = gender
        self.maxHp = health

    # Method for damage for a Pokemon.
    def damaged(self, damage):
        # Set health to zero if the damage is greater than the health
        if self.health - damage <= 0:
            self.health = 0
            return 0
        # Otherwise, reduce the health normally
        self.health -= damage
        return self.health

    # Method for printing out the information related to the Pokemon such as name, species, health, type of pokemon,
    # nature, and gender
    def print_mon(self):
        print(
            f"\nName: {self.name}\nSpecies: {self.species}\nHealth: {self.health} / {self.maxHp}\nType: {self.type_of_pokemon}\nNature: {self.nature}\nGender: {self.gender}")
        print("Moves and Power")
        for i in self.moves:
            print(i.name, i.power)

    # print out the moves with the index, name and power
    def print_moves(self):
        print("Moves and Power")
        for index, i in enumerate(self.moves):
            print(index + 1, i.name, i.power)

# Class for Pokemon Moves.
#Expects the name of the move and the power
class PokemonMoves:
    def __init__(self, name, power):
        self.name = name
        self.power = power


# initialize some pokemon moves for the game
psychic = PokemonMoves("Psychic", 80)
focus_blast = PokemonMoves("Focus Blast", 100)
shadow_ball = PokemonMoves("Shadow Ball", 80)
earthquake = PokemonMoves("Earthquake", 100)
thunderbolt = PokemonMoves("Thunderbolt", 90)
quick_attack = PokemonMoves("Quick Attack", 40)
rock_smash = PokemonMoves("Rock Smash", 40)
hydro_pump = PokemonMoves("Hydro Pump", 120)
flash_cannon = PokemonMoves("Rock Smash", 80)
surf = PokemonMoves("Rock Smash", 95)
ice_beam = PokemonMoves("Rock Smash", 95)
dragon_pulse = PokemonMoves("Dragon Pulse", 85)
dragon_ascent = PokemonMoves("Dragon Ascent", 120)
crunch = PokemonMoves("Crunch", 80)
dark_pulse = PokemonMoves("Dark Pulse", 80)
flamethrower = PokemonMoves("Flamethrower", 90)
bite = PokemonMoves("Bite", 60)
rest = PokemonMoves("Rest", 0)
amnesia = PokemonMoves("Amnesia", 0)
stockpile = PokemonMoves("Stockpile", 0)
lock_on = PokemonMoves("Lock On", 0)
tackle = PokemonMoves("Tackle", 40)
recycle = PokemonMoves("Recycle", 0)
psybeam = PokemonMoves("Psybeam", 65)

# initialize some pokemon to use for the game
mew_two = Pokemon("Mewtwo", "Mewtwo", "Psychic", "Serious",
                  [psychic, focus_blast, shadow_ball, earthquake], 416,
                  "Genderless")
pikachu = Pokemon("Pikachu", "Pikachu", "Electric", "Naughty", [thunderbolt, quick_attack, rock_smash, tackle], 283,
                  "Male")
blastoise = Pokemon("Blastoise", "Blastoise", "Water", "Calm",
                    [hydro_pump, flash_cannon, surf, ice_beam], 300, "Male")
rayquaza = Pokemon("Rayquaza", "Rayquaza", "Dragon", "Modest",
                   [earthquake, dragon_ascent, dragon_pulse, crunch], 414, "Genderless")
charizard = Pokemon("Charizard", "Charizard", "Fire", "Hasty",
                    [earthquake, flamethrower, dragon_pulse, crunch], 300, "Male")
lapras = Pokemon("Lapras", "Lapras", "Water", "Calm",
                 [surf, ice_beam, hydro_pump, crunch], 280, "Female")
weavile = Pokemon("Weavile", "Weavile", "Dark", "Quirky",
                  [crunch, ice_beam, dark_pulse, shadow_ball], 344, "Male")
sharpedo = Pokemon("Sharpedo", "Sharpedo", "Dark", "Adamant",
                   [crunch, hydro_pump, surf, ice_beam], 344, "Female")
arcanine = Pokemon("Arcanine", "Arcanine", "Fire", "Jolly",
                   [crunch, flamethrower, bite, rock_smash], 384, "Male")
snorlax = Pokemon("Snorlax", "Snorlax", "Normal", "Quiet",
                  [rest, amnesia, stockpile, focus_blast], 524, "Female")
porygon = Pokemon("Porygon", "Porygon", "Normal", "Timid",
                  [psybeam, tackle, recycle, lock_on], 334, "Genderless")
weavile2 = Pokemon("Weavile", "Weavile", "Dark", "Quirky",
                   [crunch, ice_beam, dark_pulse, shadow_ball], 344, "Male")
arcanine2 = Pokemon("Arcanine", "Arcanine", "Fire", "Jolly",
                    [crunch, flamethrower, bite, rock_smash], 384, "Male")
