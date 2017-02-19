import character
import inventory
import arena
from action import *


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

    # for item in Item.items_list :
    #     print type(item).__name__

    # for k, v in Character.characters_dict.iteritems() :
    #    print k, v

    print "Choosing Aragorn ..."
    print character.aragorn

    print "Aragorn picks Anduril ..."
    character.aragorn.pick_item(inventory.anduril)

    print character.aragorn.item

    character.lurtz.pick_item(inventory.morgul_blade)

    combat(arena.moria, character.aragorn, character.lurtz)

    # for k, v in character.aragorn.items.iteritems():
    #    print k, v.name, v.impact, v.regen_time

    # print "Or would you like to create a character ?"
    # create_character(name="Thingol", race="Elf", attributes=(90, 90, 90))

    """
    print "Welcome to Middle Earth"
    print "-----------------------"
    time.sleep(1)
    print "Choose a character"
    print "Alliance characters are : Gandalf, Frodo, Sam, Aragorn, Legolas, Gimli, Faramir, Eomer, Treebeard, Eowyn"
    print "Mordor characters are : Sauron, Saruman, Witch King, Balrog of Moria, Gollum, Shelob, Gorbag, Lurtz"
    print "-----------------------"


    choice = random.randrange(len(Character.characters_list))
    hero = Character.characters_list[choice]
    print "You have chosen :", hero.name
    time.sleep(1)
    print "Finding a worthy opponent ..."
    time.sleep(1)
    choice = random.randrange(len(Character.characters_list))
    opponent = Character.characters_list[choice]
    print opponent.name, "challenges you to a fight !"
    print "-----------------------"
    time.sleep(1)

    print "Choose an item"
    print "Items available are : Anduril, Sting, Glamdring, The One Ring, " \
          "Phial of Galadriel, Staff of Gandalf, Bow of Legolas, Gimli's Axe, Morgul Blade"
    choice = random.randrange(len(Item.items_list))
    hero_item = Item.items_list[choice]
    print "You are now equipped with :", hero_item.name
    choice = random.randrange(len(Item.items_list))
    opponent_item = Item.items_list[choice]
    print opponent.name, "has chosen to fight you with:", opponent_item.name
    print "-----------------------"
    time.sleep(1)

    print "Assigning a battle arena"
    choice = random.randrange(len(Arena.arena_list))
    arena = Arena.arena_list[choice]
    print "You will now do battle at: ", arena.name
    print "Fight !"
    victor = combat(hero, opponent)
    print "xxxxxxxxxxxxxxxxxxxxxxx"
    print "To the victor : ", victor.name, ", go the spoils!"
    """

if __name__ == "__main__":
    main()
