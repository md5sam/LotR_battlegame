class Arena(object):
    arena_list = []
    advantage = ()
    disadvantage = ()

    def __init__(self, name, allegiance):
        self.name = name
        self.allegiance = allegiance
        self.arena_list.append(self)


class Mountain(Arena):
    """

    """
    advantage = ('Wizard',)
    disadvantage = ('Dwarf')


class Mine(Arena):
    """

    """
    advantage = ('Dwarf', 'Maiar', 'Orc', 'UrukHai',)
    disadvantage = ('Wizard',)


class Battlefied(Arena):
    """

    """
    disadvantage = ('Ent', 'Maiar', 'Hobbit',)


class City(Arena):
    """

    """
    advantage = ('Hobbit',)


class Forest(Arena):
    """

    """
    advantage = ('Ent', 'Elf')
    disadvantage = ('Orc', 'UrukHai')


class Fortress(Arena):
    """

    """


def generate_arenas():
    global caradhras
    caradhras = Mountain("The Pass of Caradhras", 0)
    global moria
    moria = Mine("The Mines of Moria", 0)
    global pelennor
    pelennor = Battlefied("Pelennor Fields", 1)
    global minas_tirith
    minas_tirith = City("Minas Tirith", 1)
    global fangorn
    fangorn = Forest("Fangorn Forest", 1)
    global helms_deep
    helms_deep = Fortress("Helm's Deep", 1)

# generate_arenas()
