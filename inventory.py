from collections import defaultdict, OrderedDict, namedtuple


class Item(object) :
    items_list = []

    def __init__(self, name, impact, regen_time):
        """
        :param name:
        :param impact: amount of damage / healing points
        :param regen_time: in seconds
        :return:
        """
        self.name = name
        self.impact = impact
        self.regen_time = regen_time
        self.items_list.append(self)

class Weapon(Item):
    """ the general class of weapons
    """


class MagicalObject(Item):
    """
    rings, staffs, vial of Galadriel
    """


class MeleeWeapon(Weapon):
    """
    swords, axes, staffs
    """


class RangedWeapon(Weapon):
    """
    bow-arrow, siege weaponry
    """


def populate_inventory() :
    anduril = MeleeWeapon("Anduril", 50, 1)
    sting = MeleeWeapon("Sting", 30, 1)
    glamdring = MeleeWeapon("Glamdring", 30, 1)
    one_ring = MagicalObject("One Ring", 50, 1)
    phial_galadriel = MagicalObject("Phial of Galadriel", 20, 2)
    staff_gandalf = MagicalObject("Staff of Gandalf", 50, 1)
    bow_legolas = RangedWeapon("Bow of Legolas", 30, 1)
    axe_gimli = MeleeWeapon("Gimli's Axe", 30, 1)
    morgul_blade = MeleeWeapon("Morgul Blade", 40, 1)

populate_inventory()