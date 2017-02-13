from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple

class Character(object):
    """ stores character attributes and methods """
    _characters_dict = defaultdict(list)
    characters_list = []
    ability = "undeclared"
    Attributes = namedtuple('Attributes', 'strength agility intelligence')

    def __init__(self, name, *attributes):
        """
        :param name: "Name"
        :param *attributes : strength : / 100, agility : / 100, intelligence : / 100
        :return:
        """
        self.name = name
        self.attributes = self.Attributes(*attributes)
        self.items = self
        self.characters_list.append(self)
        self._characters_dict[type(self).__name__].append(self.name)

    def declare_name(self):
        print "My name is ", self.name, "of race", type(self).__name__

    def declare_ability(self):
        print "My ability is : ", self.ability

    def declare_attributes(self):
        print self.attributes

    @classmethod
    def strongest_character(cls):
        """ iterates through every character created so far and prints strongest """
        max_strength = 0
        #strongest = None
        for character in cls.characters_list:
            if character.attributes.strength > max_strength:
                strongest = character
        print "The strongest character alive is :", strongest.name


    @classmethod
    def _show_all_characters(cls) :
        for k, v in cls._characters_dict.iteritems() :
            print k, v 


class Orc(Character):
    """ the orc class has extra attributes and methods
    attributes : master
    methods : declare_allegiance 
    """
    master = "Sauron"

    def declare_allegiance(self):
        print "I serve", self.master


class Goblin(Character):
    """ """
    ability = "I fear not the light of sun !"


class UrukHai(Orc, Goblin):
    """ """
    master = "Saruman"


class Elf(Character):
    """ """
    ability = "I fear no mortal death"


class Dwarf(Character):
    """ """


class Human(Character):
    """ """


class Nazgul(Human):
    """ """
    master = "Sauron"


class Ent(Character):
    """
    """


class Maiar(Character) :
    """

    """


class Wizard(Maiar) :
    """

    """


class Hobbit(Character) :
    """
    """


def spawn_characters ():
    gandalf = Wizard("Gandalf", *(91, 85, 97))
    frodo = Hobbit("Frodo", *(91, 85, 97))
    sam = Hobbit("Sam", *(91, 85, 97))
    aragorn = Human("Aragorn", *(91, 85, 97))
    legolas = Elf("Legolas", *(91, 85, 97))
    gimli = Dwarf("Gimli", *(91, 85, 97))
    faramir = Human("Faramir", *(91, 85, 97))
    eomer = Human("Eomer", *(91, 85, 97))
    eowyn = Human("Eowyn", *(91, 85, 97))
    treebeard = Ent("Treebeard", *(91, 85, 97))
    gollum = Hobbit("Gollum", *(91, 85, 97))
    sauron = Maiar("Sauron", *(91, 85, 97))
    saruman = Wizard("Saruman", *(91, 85, 97))
    witch_king = Human("Witch King of Angmar", *(91, 85, 97))
    balrog = Maiar("Balrog of Moria", *(91, 85, 97))
    shelob = Maiar("Shelob", *(91, 85, 97))
    gorbag = Orc("Gorbag", *(91, 85, 97))
    lurtz = UrukHai("Lurtz", *(91, 85, 97))

spawn_characters()


