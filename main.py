from character import *
from inventory import *
from arena import *
from action import *


def main():
    """
    namedtuple order is Strength Agility Intelligence
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

if __name__ == "__main__":
    main()






    '''
    gorbag = Orc("Gorbag", *(79,82,64))
    gorbag.declare_name()
    gorbag.declare_allegiance()
    shagrat = Orc("Shagrat", *(78, 81, 68))

    lurtz = UrukHai("Lurtz", *(85,81,82))
    lurtz.declare_name()
    lurtz.declare_allegiance()
    lurtz.declare_ability()

    aragorn = Human("Aragorn", *(94,93,92))
    aragorn.declare_attributes()

    Character.strongest_character()
    print "Going to show all characters"
    Character._show_all_characters()

    victor = combat(aragorn, gorbag)
    '''
    #print "To the victor : ", victor.name, ", go the spoils!"