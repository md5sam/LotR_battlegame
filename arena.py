class Arena(object) :
    arena_list = []
    def __init__(self, name, allegiance):
        self.name = name
        self.allegiance = allegiance
        self.arena_list.append(self)

class Mountain(Arena) :
    """

    """


class Mine(Arena) :
    """

    """


class Battlefied(Arena) :
    """

    """


class City(Arena) :
    """

    """


class Forest(Arena) :
    """

    """


class Fortress(Arena) :
    """

    """


def generate_arenas():
    caradhras = Mountain("The Pass of Caradhras",0)
    moria = Mine("The Mines of Moria",0)
    pelennor = Battlefied("Pelennor Fields", 1)
    minas_tirith = City("Minas Tirith", 1)
    fangorn = Forest("Fangorn Forest", 1)
    helms_deep = Fortress("Helm's Deep", 1)


generate_arenas()
