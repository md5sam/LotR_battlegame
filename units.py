import character


# Level 0 Class is below (base class, NOT abstract)
class Unit(object):
    soldiers = []
    infantry_a, siege_a, melee_a, ranged_a = 0, 0, 0, 0
    infantry_d, siege_d, melee_d, ranged_d = 0, 0, 0, 0

    def __init__(self, characters):
        for character.Character in characters:
            self.soldiers.append(character)

    def __repr__(self):
        """
        define how the characters in the unit prints out
        """

    def __iter__(self):
        """
        define how the characters can be iterated
        :return:
        """

    def next(self):
        """
        for iteration
        :return:
        """


# Level 1 Classes are below
class Alliance(Unit, character.Wizard, character.Elf, character.Human, character.Dwarf,
               character.Hobbit, character.Ent):
    """
    a base class of "good" characters
    """


class Horde(Unit, character.DarkMaiar, character.Nazgul, character.UrukHai, character.Orc, character.Goblin):
    """
    a base class of Sauron's units
    """


# Level 2 classes start here
class HumanArmy(character.Human, Alliance):
    """

    """


class DwarvenArmy(character.Dwarf, Alliance):
    """

    """


class ElvenArmy(character.Elf, Alliance):
    """

    """


class EntMoot(character.Ent, Alliance):
    """

    """


class UrukArmy(character.UrukHai, Horde):
    """

    """


class OrcArmy(character.Orc, Horde):
    """

    """


class GoblinArmy(character.Goblin, Horde):
    """

    """


class BlackRiders(character.Nazgul, Horde):
    """

    """


# Level 3 classes start here
class Rohirrim(HumanArmy):
    """
    a special class of human army (available in map of Rohan)
    +10 cavalry bonus
    +5 infantry attack
    """


class GuardsOfTheCitadel(HumanArmy):
    """
    a special class of human army (available in map of Gondor)
    +10 ranged bonus
    +5 siege attack
    +5 siege defense
    """


class LastAlliance(character.Elf, character.Human, Alliance):
    """
    a special case of the Alliance led by Elves and Men
    """


class Fellowship(AllianceABC):
    """
    a special case of the Alliance led by a Wizard
    """


class WhiteCouncil(AllianceABC):
    """
    a special case of the Alliance led by a Wizard
    """


def create_custom_unit(unit_name):
    """
    This function creates custom units that the user specifies
    :param unit_name:
    :return:
    """
    # use __type__ to create a class factory
    # class unit_name (Unit) :
    #   attributes go here ...

