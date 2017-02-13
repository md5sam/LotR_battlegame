from character import *
from inventory import *
from arena import *
import time
import random


def combat(character1, character2):
    print "Prepare for combat between", character1.name, "and", character2.name, "!"
    time.sleep(2)

    ch1_score = 0
    ch2_score = 0

    for round_number in range(1,4):
        print "Round :", round_number, "has begun... FIGHT!"

        attb_choice = random.randrange(2)
        print "Attribute chosen to fight with is :", Character.Attributes._fields[attb_choice]

        if character1.attributes[attb_choice] > character2.attributes[attb_choice] :
            ch1_score += 1

        elif character2.attributes[attb_choice] > character1.attributes[attb_choice] :
            ch2_score += 1

    if ch1_score > ch2_score :
        print character2.name, "is vanquished!"
        return character1
    else:
        print character1.name, "is vanquished!"
        return character2


def effect_multiplier (item1, item2) :
    outcomes = {(MeleeWeapon, RangedWeapon): item2,
                (RangedWeapon, MeleeWeapon): item1,
                (MagicalObject, MeleeWeapon): item2,
                (MeleeWeapon, MagicalObject): item1,
                (RangedWeapon, MagicalObject): item2,
                (MagicalObject, RangedWeapon): item1,
                (MeleeWeapon, MeleeWeapon): None,
                (RangedWeapon, RangedWeapon): None,
                (MagicalObject, MagicalObject): None
                }

    item1_type = type(item1).__name__
    item2_type = type(item2).__name__

    advantage = outcomes[(item1_type, item2_type)]
    return advantage
