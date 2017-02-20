import random
import time
import character
import inventory
import action
import arena


def main():
    """
    set up and teardown here
    namedtuple order is Strength Agility Intelligence
    """
    character.spawn_characters()
    inventory.populate_inventory()
    arena.generate_arenas()

    # access all characters ONLY through Character class attribute : Character.character_lists
    # access all items ONLY through Item class attribute : Item.items_list

    print "Welcome to Middle Earth"
    print "-----------------------"
    time.sleep(1)
    print "Choose a character"
    print "Alliance characters are : Gandalf, Frodo, Sam, Aragorn, Legolas, Gimli, Faramir, Eomer, Treebeard, Eowyn"
    print "Mordor characters are : Sauron, Saruman, Witch King, Balrog of Moria, Gollum, Shelob, Gorbag, Lurtz"
    print "-----------------------"

    choice = random.randrange(len(character.Character.characters_list))
    hero = character.Character.characters_list[choice]
    print "You have chosen :", hero.name
    time.sleep(1)
    print "Finding a worthy opponent ..."
    time.sleep(1)
    choice = random.randrange(len(character.Character.characters_list))
    opponent = character.Character.characters_list[choice]
    print opponent.name, "challenges you to a fight !"
    print "-----------------------"
    time.sleep(1)

    print "Choose an item"
    print "Items available are : Anduril, Sting, Glamdring, The One Ring, " \
          "Phial of Galadriel, Staff of Gandalf, Bow of Legolas, Gimli's Axe, Morgul Blade"
    choice = random.randrange(len(inventory.Item.items_list))
    hero.pick_item(inventory.Item.items_list[choice])
    print "You are now equipped with :", hero.item.name
    choice = random.randrange(len(inventory.Item.items_list))
    opponent.pick_item(inventory.Item.items_list[choice])
    print opponent.name, "has chosen to fight you with:", opponent.item.name
    print "-----------------------"
    time.sleep(1)

    print "Assigning a battle arena"
    choice = random.randrange(len(arena.Arena.arena_list))
    curr_arena = arena.Arena.arena_list[choice]
    print "You will now do battle at: ", curr_arena.name
    print "Fight !"
    victor = action.combat(curr_arena, hero, opponent)
    print "xxxxxxxxxxxxxxxxxxxxxxx"
    print "To the victor : ", victor.name, ", go the spoils!"


if __name__ == "__main__":
    main()
