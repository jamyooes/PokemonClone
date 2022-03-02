"""
This is our main file which imports all the other files and is our game logic and view.
There are various helper functions to help with basic printing
Author: James Yoo
"""

from BagFile import *
from PlayerFile import *
from GameMapFile import *
from PokemonFile import *
import random


# this function will be invoked in the beginning of the program to create a character and player
def character_creation():
    # user can choose their avatar from 8 choices
    avatar = ""
    print("Select your avatar")
    print("Enter 1 for 👺")
    print("Enter 2 for 👹")
    print("Enter 3 for 🤡")
    print("Enter 4 for 💩")
    print("Enter 5 for 🤡")
    print("Enter 6 for ☠")
    print("Enter 7 for 👽")
    print("Enter 8 for 🤖")
    character = int(input("Enter the number for the avatar: "))
    # if the user enters an invalid number give the user another chance to enter an input for avatar
    while character > 8 or character <= 0:
        print("Invalid input try again 😅")
        print("Enter 1 for 👺")
        print("Enter 2 for 👹")
        print("Enter 3 for 🤡")
        print("Enter 4 for 💩")
        print("Enter 5 for 🤡")
        print("Enter 6 for ☠")
        print("Enter 7 for 👽")
        print("Enter 8 for 🤖")
        character = int(input("Enter the number for the avatar: "))
    # set the avatar to the user's choice
    if character == 1:
        avatar = "👺"
    elif character == 2:
        avatar = "👹"
    elif character == 3:
        avatar = "🤡"
    elif character == 4:
        avatar = "💩"
    elif character == 5:
        avatar = "🤡"
    elif character == 6:
        avatar = "☠"
    elif character == 7:
        avatar = "👽"
    else:
        avatar = "🤖"
    # set the user's name
    print("\n")
    name = input("Enter your name: ")

    # choice for gender male or female
    gender = ""
    print("\n")
    print("Enter 1 if you are a male")
    print("Enter 2 if you are a female")
    gender_choice = int(input("Enter gender: "))
    while gender_choice > 2 or gender_choice < 1:
        print("Enter 1 if you are a male")
        print("Enter 2 if you are a female")
        gender_choice = int(input("Enter gender: "))
    if gender_choice == 1:
        gender = "Male"
    elif gender_choice == 2:
        gender = "Female"

    # user can enter their own nature whetehr a word or sentence
    print("\n")
    nature = input("Enter your nature: ")

    # creating bag (two revives because of the difficulty of the game)
    bag = Bag()
    bag.add_item("Revive")
    bag.add_item("Revive")

    # user's starting pokemon choices
    print("\n")
    starting_mon = ""
    print("Choose your pokemon")
    print("Enter 1 for Mewtwo")
    print("Enter 2 for Pikachu")
    print("Enter 3 for Blastoise")
    pokemon_choice = int(input("Enter your choice: "))
    while pokemon_choice > 3 or pokemon_choice < 1:
        print("Invalid input choose your pokemon")
        print("Enter 1 for Mewtwo")
        print("Enter 2 for Pikachu")
        print("Enter 3 for Blastoise")
        pokemon_choice = int(input("Enter your choice: "))
    if pokemon_choice == 1:
        starting_mon = mew_two
    elif pokemon_choice == 2:
        starting_mon = pikachu
    else:
        starting_mon = blastoise

    # rename the pokemon for the starter
    print("\n")
    rename_choice = int(input("Rename your pokemon? \nEnter 1 to rename, enter 0 to not rename: "))
    while rename_choice > 1 or rename_choice < 0:
        print("Invalid input. \nEnter 1 to rename, enter 0 to not rename: ")
        rename_choice = int(input("Enter your choice: "))
    if rename_choice == 1:
        new_name = input("Enter your pokemon's new name: ")
        starting_mon.name = new_name
    print("\n")
    print("\n")
    # returns all information  needed to create a pokemon trainer/ player
    return avatar, Player(name, [starting_mon], bag, 0, gender, nature)


# this is to create a option to return to the map. This allows the user time to view their own menus such as their bag
def return_to_grid_from_menu(escape=1):
    if escape == 0:
        return
    while True:
        exit_menu_choice = input("return to map with 0: ")
        if exit_menu_choice == "0":
            break


# Helper function to print out all pokemon in the list the user can enter the pokemon's index to view more infromation
# about the pokemon
def pokemon_prints(pokemon_list):
    print("Index, Pokemon Name, Percent HP remaining")
    for index, pokemon in enumerate(pokemon_list):
        print(index + 1, pokemon.name, round((pokemon.health / pokemon.maxHp) * 100, 0))
    choice = int(input("Check the pokemon information by entering the index or enter 0 to leave the menu: "))
    if choice == 0:
        return 0
    print("\n\n")
    while choice - 1 >= len(pokemon_list) or choice < 1:
        print("Index, Pokemon Name, Percent HP remaining")
        for index, pokemon in enumerate(pokemon_list):
            print(index + 1, pokemon.name, round((pokemon.health / pokemon.maxHp) * 100, 0))
        choice = int(
            input("Invalid Input, Check the pokemon information by entering the index or enter 0 to leave the menu: "))
        if choice == 0:
            return 0
        print("\n\n")
    pokemon_list[choice - 1].print_mon()


# instantiated cpus
dracula = CPU("Pokemon Trainer Darcula", [sharpedo, weavile], 9999, weavile2, "I am not a vampire")
baby = CPU("Baby Manda", [snorlax], 1, None, "I stole this pokemon from my mom")
police = CPU("Police Officer Coppa", [arcanine], 500, arcanine2, "I am scared of vampires")
lady = CPU("Lady Flora", [porygon], 2000, None, "I like computers")


# interact function when the user talks to a trainer or box
def interact(board, trainer):
    user_position_row = board.player_loc[0]
    user_position_col = board.player_loc[1]
    # can only interact with dracula cpu from the left on our premade map
    if board.actual_board[user_position_row][user_position_col - 1] == "🧛" and dracula.defeated == False:
        win_loss = battle(trainer, dracula)
        return_to_grid_from_menu()
        return win_loss
    # can only interact with the police cpu from the left
    elif board.actual_board[user_position_row][user_position_col - 1] == "👮" and police.defeated == False:
        win_loss = battle(trainer, police)
        return_to_grid_from_menu()
        return win_loss
    # can only interact with the baby cpu from the left and bottom
    elif board.actual_board[user_position_row][user_position_col - 1] == "👶" or \
            board.actual_board[user_position_row - 1][user_position_col] == "👶" and baby.defeated == False:
        win_loss = battle(trainer, baby)
        return_to_grid_from_menu()
        return win_loss
    # can only interact with the lady cpu from the right
    elif board.actual_board[user_position_row][user_position_col + 1] == "👧" and lady.defeated == False:
        win_loss = battle(trainer, lady)
        return_to_grid_from_menu()
        return win_loss
    # interact with the pokeball represented as a present box, free pokemon
    elif board.actual_board[user_position_row][user_position_col - 1] == "🎁":
        trainer.pokemon_list.append(lapras)
        print("Lapras has been added to your party")
        board.actual_board[user_position_row][user_position_col - 1] = "⬜"
        return_to_grid_from_menu()
        return 0
    # interact with the pokeball represented as a present box, free pokemon
    elif board.actual_board[user_position_row][user_position_col + 1] == "🎁":
        trainer.pokemon_list.append(charizard)
        print("Charizard has been added to your party")
        board.actual_board[user_position_row][user_position_col + 1] = "⬜"
        return_to_grid_from_menu()
        return 0
    # interact with the pokeball represented as a present box, free pokemon
    elif board.actual_board[user_position_row + 1][user_position_col] == "🎁" or board.actual_board[user_position_row][
        user_position_col - 1] == "🎁":
        trainer.pokemon_list.append(rayquaza)
        print("Rayquaza has been added to your party")
        board.actual_board[user_position_row][user_position_col + 1] = "⬜"
        return_to_grid_from_menu()
        return 0
    else:
        return 0


# this is a helper function for the battle function to select our pokemon in the beginning of the battle
def selectActivePokemon(pokemon_list):
    for pokemons in pokemon_list:
        if pokemons.health > 0:
            return pokemons
    return None


# this is a helper function for the battle function to select our pokemon in the user's turn
def choice_swap(pokemon, pokemon_lists):
    print("Index, Pokemon Name, Percent HP remaining")
    for index, pokemon in enumerate(pokemon_lists):
        print(index + 1, pokemon.name, round((pokemon.health / pokemon.maxHp) * 100, 0))
    choice = int(input("Swap the pokemon by entering the index or enter [0] to go back"))
    if choice == 0:
        return 0
    while pokemon_lists[choice - 1].health == 0 or choice > len(pokemon_lists) or choice < 0:
        choice = int(input("Can't swap fainted pokemon, swap the pokemon by entering the index"))
    return pokemon_lists[choice - 1]


# this is a helper function for the battle function to select pokemon when teh pokemon has fainted and must choose a pokemon
def mandatory_swap(pokemon_list):
    # return None if the pokemon are all fainted
    count_alive = 0
    for pokemon in pokemon_list:
        if pokemon.health > 0:
            count_alive += 1
    if count_alive == 0:
        return None
    # otherwise the user can select a pokemon to swap into
    print("Index, Pokemon Name, Percent HP remaining")
    for index, pokemon in enumerate(pokemon_list):
        print(index + 1, pokemon.name, round((pokemon.health / pokemon.maxHp) * 100, 0))
    choice = int(input("Swap the pokemon by entering the index"))
    while pokemon_list[choice - 1].health == 0:
        choice = int(input("Can't swap fainted pokemon, swap the pokemon by entering the index"))
    return pokemon_list[choice - 1]


# this is a helper function for the user to choose a move to fight with
def use_move(pokemon, choice):
    return pokemon.moves[choice - 1].name, pokemon.moves[choice - 1].power


# this is a helper function for the cpu's move in their turn of the battle, which will be randomized
def cpu_move(pokemon):
    choice = random.randint(0, 3)
    return pokemon.moves[choice].name, pokemon.moves[choice].power


# this is our battle function which will be triggered when the user interacts with the cpu on the overworld
def battle(player1, player2):
    print(f"{player1.name} challenges {player2.name} to a battle\n\n")
    # choose the first non-fainted pokemon from each player's pokemon list
    active_pokemon_1 = selectActivePokemon(player1.pokemon_list)
    active_pokemon_2 = selectActivePokemon(player2.pokemon_list)
    # the battle will continuously loop there are some return statements that will break this loop and return to
    # the overworld
    while True:
        # print statements for the user to view their own pokemon and opponent pokemon's health
        print(
            f'{player2.name}\'s {active_pokemon_2.name}------{active_pokemon_2.health} / {active_pokemon_2.maxHp}\n\n'
            f'\n\n')
        print(
            f'{player1.name}\'s {active_pokemon_1.name}------{active_pokemon_1.health} / {active_pokemon_1.maxHp}\n\n'
            f'\n\n')
        # options for the user during the battle
        battle_option = int(input("[1] Fight\n[2] Run\n[3] Bag\n[4] Change Pokemon\n"))
        # option to run away leaves the battle function
        if battle_option == 2:
            print("You ran away!!!")
            return
        # choice to use an item in the bag
        elif battle_option == 3:
            back = 0
            player1.bag.print_contents()
            # option to use an item or exit the bag menu
            bag_option = int(input("Enter the bag index to use item, enter 0 to exit bag: "))
            print("\n")
            if bag_option != 0:
                # call the bag menu to use item
                back = main_player.bag.use_item(bag_option, main_player.pokemon_list)
            # return to the battle state if leaving the bag
            elif back == 0:
                continue
            else:
                continue
            print(
                f'{player2.name}\'s {active_pokemon_2.name}------{active_pokemon_2.health} / {active_pokemon_2.maxHp}\n\n'
                f'\n\n')
            print(
                f'{player1.name}\'s {active_pokemon_1.name}------{active_pokemon_1.health} / {active_pokemon_1.maxHp}\n\n'
                f'\n\n')
            # set up the cpu's move
            move_name_2, move_power_2 = cpu_move(active_pokemon_2)
            print(f'{player2.name}\'s {active_pokemon_2.name} used {move_name_2}!')
            # inflict damage to the player's pokemon
            active_pokemon_1.damaged(move_power_2)
            # swap pokemon if the cpu's pokemon does enough damage to reduce the player's pokemon health to 0
            if active_pokemon_1.health == 0:
                active_pokemon_1 = mandatory_swap(player1.pokemon_list)
                # player loses if they have no more pokemon to swap to
                if active_pokemon_1 is None:
                    print(f"You Lost!!!\n")
                    return -1
        # if the player decides to select a move to fight
        elif battle_option == 1:
            active_pokemon_1.print_moves()
            # this option is in case the user wants to go back the fight menu
            go_back = int(input("Enter [0] to go back and [7] to continue: "))
            while go_back not in [0, 7]:
                go_back = int(input("Enter [0] to go back and [7] to continue: "))
            # go back to the fight menu
            if go_back == 0:
                continue
            # user selects a move
            select_move = int(input("Select move to use [1],[2],[3],[4]: "))
            while select_move not in [1, 2, 3, 4]:
                print(
                    f'{player2.name}\'s {active_pokemon_2.name}------{active_pokemon_2.health} / {active_pokemon_2.maxHp}\n\n'
                    f'\n\n')
                print(
                    f'{player1.name}\'s {active_pokemon_1.name}------{active_pokemon_1.health} / {active_pokemon_1.maxHp}\n\n'
                    f'\n\n')
                active_pokemon_1.print_moves()
                select_move = int(input("Select move to use [1],[2],[3],[4]: "))
            move_name_1, move_power_1 = use_move(active_pokemon_1, select_move)
            print(f'{player1.name}\'s {active_pokemon_1.name} used {move_name_1}!')
            # deal damage to cpu's pokemon
            active_pokemon_2.damaged(move_power_1)
            # if cpu's pokemon faints then the cpu will select their next pokemon
            if active_pokemon_2.health == 0:
                active_pokemon_2 = selectActivePokemon(player2.pokemon_list)
                # if the cpu has no more pokemon then the player wins and will receive a bunch of rewards
                if active_pokemon_2 is None:
                    player2.defeated = True
                    print(f"{player2.name}: {player2.fact}")
                    player1.money += player2.reward_money
                    print(f"You won!!!\nYou won {player2.reward_money} and a Full Restore")
                    player1.bag.add_item("Full Restore")
                    if player2.gift_pokemon is not None:
                        player1.pokemon_list.append(player2.gift_pokemon)
                        print(f"{player2.name} gifted you {player2.gift_pokemon.name}!!!\n")
                    return 0
            # if the cpu's pokemon survives then the cpu's pokemon will attack
            else:
                print(
                    f'{player2.name}\'s {active_pokemon_2.name}------{active_pokemon_2.health} / {active_pokemon_2.maxHp}\n\n'
                    f'\n\n')
                print(
                    f'{player1.name}\'s {active_pokemon_1.name}------{active_pokemon_1.health} / {active_pokemon_1.maxHp}\n\n'
                    f'\n\n')
                move_name_2, move_power_2 = cpu_move(active_pokemon_2)
                print(f'{player2.name}\'s {active_pokemon_2.name} used {move_name_2}!')
                active_pokemon_1.damaged(move_power_2)
                # if the cpu's pokemon defeats the player pokemon then the player must swap otherise it is their loss
                if active_pokemon_1.health == 0:
                    active_pokemon_1 = mandatory_swap(player1.pokemon_list)
                    if active_pokemon_1 is None:
                        print(f"You Lost!!!\n")
                        return -1
        # option for the user to swap their current pokemon
        elif battle_option == 4:
            swap = choice_swap(active_pokemon_1, player1.pokemon_list)
            if swap == 0:
                continue
            else:
                active_pokemon_1 = swap
            print(
                f'{player2.name}\'s {active_pokemon_2.name}------{active_pokemon_2.health} / {active_pokemon_2.maxHp}\n\n'
                f'\n\n')
            print(
                f'{player1.name}\'s {active_pokemon_1.name}------{active_pokemon_1.health} / {active_pokemon_1.maxHp}\n\n'
                f'\n\n')
            # after the swap the user's pokemon will take damage
            move_name_2, move_power_2 = cpu_move(active_pokemon_2)
            print(f'{player2.name}\'s {active_pokemon_2.name} used {move_name_2}!')
            active_pokemon_1.damaged(move_power_2)
            if active_pokemon_1.health == 0:
                active_pokemon_1 = mandatory_swap(player1.pokemon_list)
                if active_pokemon_1 is None:
                    print(f"You Lost!!!\n")
                    return -1


def board_actions(board):
    while True:
        # win-condition and break from the game is when the user is in possession of 4 unique pokemon
        caught = len(main_player.pokemon_list)
        if caught == 4:
            print("\n\n\n\n\n\n\nYou won!!!")
            break
        # view the grid
        my_board.print_grid()
        # player input for menus or movement
        player_movement = input("Move left (a), Move right (d), Move up(w), Move Down (s), Bag(i), Interact with NPC "
                                "or boxes(q), check id with (id), check pokemon with (p): ")
        while player_movement not in ["w", "a", "s", "d", "i", "id", "p", "q"]:
            print("\n\n\n")
            my_board.print_grid()
            player_movement = input("Invalid Input, Move left (a), Move right (d), Move up(w), Move Down (s), Bag(i), "
                                    "Interact with NPC or boxes(q), check id with (id), check pokemon with (p): ")
        # player movement
        if player_movement in ["w", "a", "s", "d"]:
            my_board.update_movement(player_movement)
        # bag menu
        elif player_movement == "i":
            main_player.bag.print_contents()
            bag_option = int(input("Enter the bag index to use item, enter 0 to exit bag: "))
            print("\n")
            if bag_option != 0:
                main_player.bag.use_item(bag_option, main_player.pokemon_list)
            return_to_grid_from_menu(bag_option)
        # player id meny
        elif player_movement == "id":
            print(main_player)
            return_to_grid_from_menu()
        # pokemon menu
        elif player_movement == "p":
            check_another = 1
            while check_another:
                if pokemon_prints(main_player.pokemon_list) == 0:
                    break
                check_another = int(input("Check another pokemon? Enter 1 to check another pokemon and 0 to exit: "))
                print("\n\n")
            print("\n\n")
            return_to_grid_from_menu(0)
        # interact with pokeball or cpu
        elif player_movement == "q":
            loss = interact(my_board, main_player)
            # lose when defeated
            if loss == -1:
                print("\n\n\n\n\n\n\nGame Over :P")
                break


if __name__ == '__main__':
    # pre made grid
    gameMap = [
        ['🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳'],
        ['🌳', '🧛', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '👧'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '🌳', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '🌳', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '👶', '⬜', '⬜', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '⬜', '⬜', '⬜', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '⬜', '⬜', '🌳', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🎁', '🌳', '🎁', '⬜', '🌳', '⬜', '⬜', '🌳', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '⬜', '⬜', '🌳', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '🎁', '⬜', '⬜', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '🌳', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '🌳', '⬜', '🌳'],
        ['🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '🌳', '⬜', '🌳'],
        ['🌳', '👮', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '🌳'],
        ['🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '⬜', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳'],
        ['🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳']
    ]
    # start with character creation
    character_avatar, main_player = character_creation()
    # initialize board and user's position
    my_board = GridTiles(gameMap, character_avatar)
    # create the board
    my_board.create_board()
    # game logic
    board_actions(my_board)
