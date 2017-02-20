class Item(object):
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


def populate_inventory():
    global anduril
    anduril = MeleeWeapon("Anduril", 50, 1)
    global sting
    sting = MeleeWeapon("Sting", 30, 1)
    global glamdring
    glamdring = MeleeWeapon("Glamdring", 30, 1)
    global one_ring
    one_ring = MagicalObject("One Ring", 50, 1)
    global phial_galadriel
    phial_galadriel = MagicalObject("Phial of Galadriel", 20, 2)
    global staff_gandalf
    staff_gandalf = MagicalObject("Staff of Gandalf", 50, 1)
    global bow_legolas
    bow_legolas = RangedWeapon("Bow of Legolas", 30, 1)
    global axe_gimli
    axe_gimli = MeleeWeapon("Gimli's Axe", 30, 1)
    global morgul_blade
    morgul_blade = MeleeWeapon("Morgul Blade", 40, 1)
