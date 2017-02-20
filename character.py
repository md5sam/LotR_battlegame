from collections import defaultdict, namedtuple


class Character(object):
    _characters_dict_by_race = defaultdict(list)
    characters_list = []
    characters_dict = defaultdict(object)
    ability = "undeclared"
    Attributes = namedtuple('Attributes', 'strength agility intelligence')
    taunt = None

    def __init__(self, name, *attributes):
        """
        :param *attributes : strength : / 100, agility : / 100, intelligence : / 100
        """
        self.name = name
        self.attributes = self.Attributes(*attributes)
        self.item = None
        self.characters_list.append(self)
        self.characters_dict[self.name] = self
        self._characters_dict_by_race[type(self).__name__].append(self.name)

    def declare_name(self):
        print "My name is ", self.name, "of race", type(self).__name__

    def declare_ability(self):
        print "My ability is : ", self.ability

    def declare_attributes(self):
        print self.attributes

    def pick_item(self, item):
        self.item = item

    @classmethod
    def strongest_character(cls):
        """ iterates through every character created so far and prints strongest """
        max_strength = 0
        for character in cls.characters_list:
            if character.attributes.strength > max_strength:
                strongest = character
        print "The strongest character alive is :", strongest.name

    @classmethod
    def _show_all_characters(cls):
        for k, v in cls._characters_dict.iteritems():
            print k, v


class Orc(Character):
    """ the orc class has extra attributes and methods
    attributes : master
    methods : declare_allegiance 
    """
    master = "Sauron"

    def declare_allegiance(self):
        print "I serve", self.master

    taunt = "Lugburz will hear of this !"


class Goblin(Character):
    """ """
    taunt = "I fear not the light of sun !"


class UrukHai(Goblin, Orc):
    """ """
    master = "Saruman"


class Elf(Character):
    """ """
    taunt = "I fear no mortal death"


class Dwarf(Character):
    """ """
    taunt = "Very dangerous over short distances!"


class Human(Character):
    """ """
    taunt = "For the Alliance !"


class Nazgul(Human):
    """ """
    master = "Sauron"
    taunt = "Do not stand between a Nazgul and his prey"


class Ent(Character):
    """
    """
    taunt = "I am old as rock and mountain"


class Maiar(Character):
    """

    """


class Wizard(Maiar):
    """

    """


class Hobbit(Character):
    """
    """


def spawn_characters():
    # s a i e
    # strength agility intelligence
    global gandalf
    gandalf = Wizard("Gandalf", *(91, 85, 97))
    global frodo
    frodo = Hobbit("Frodo", *(85, 89, 91))
    global sam
    sam = Hobbit("Sam", *(86, 85, 88))
    global aragorn
    aragorn = Human("Aragorn", *(94, 91, 91))
    global legolas
    legolas = Elf("Legolas", *(91, 97, 90))
    global gimli
    gimli = Dwarf("Gimli", *(93, 85, 88))
    global faramir
    faramir = Human("Faramir", *(91, 89, 91))
    global eomer
    eomer = Human("Eomer", *(91, 89, 90))
    global eowyn
    eowyn = Human("Eowyn", *(90, 92, 90))
    global treebeard
    treebeard = Ent("Treebeard", *(94, 88, 90))
    global gollum
    gollum = Hobbit("Gollum", *(88, 93, 90))
    global sauron
    sauron = Maiar("Sauron", *(96, 90, 94))
    global saruman
    saruman = Wizard("Saruman", *(92, 84, 96))
    global witch_king
    witch_king = Human("Witch King of Angmar", *(93, 91, 90))
    global balrog
    balrog = Maiar("Balrog of Moria", *(95, 91, 90))
    global shelob
    shelob = Maiar("Shelob", *(90, 90, 90))
    global gorbag
    gorbag = Orc("Gorbag", *(86, 82, 75))
    global lurtz
    lurtz = UrukHai("Lurtz", *(90, 88, 88))


def create_character(name, race, *attributes):
    """

    :param name:
    :param race:
    :param attributes:
    :return:
    """
