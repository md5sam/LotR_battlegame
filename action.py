import time
import random
import character


def combat(arena, character1, character2):
    print "Prepare for combat between", character1.name, "and", character2.name, "!"

    time.sleep(1)
    if character1.taunt :
        print character1.name, "says :", character1.taunt
        if character2.taunt :
            print character2.name, "responds :", character2.taunt
    time.sleep(1)

    # declare scores before starting off
    ch1_score = 100
    ch2_score = 100
    print character1.name, "starts with a score of 100"
    print character2.name, "starts with a score of 100"
    time.sleep(1)


    print "Applying arena advantage ..."
    time.sleep(2)
    # calculate and adjust for arena advantage
    arena_ad = arena_advantage(arena, character1, character2)
    if str(type(character1).__name__) in arena_ad :
        ch1_score += 20
        print character1.name, "is strengthened by choice of arena : ", arena.name
    if str(type(character2).__name__) in arena_ad :
        ch2_score += 20
        print character2.name, "is strengthened by choice of arena : ", arena.name
    else:
        print "Both foes are equally matched in the choice of arena: ", arena.name

    time.sleep(1)
    print "Applying weapon class advantage ..."
    time.sleep(1)
    # calculate and adjust for item advantage
    wc_ad = weapon_class_advantage(character1.item, character2.item)
    if wc_ad == character1.item:
        ch2_score -= 20
        print character1.name, "has chosen wisely the weapon: ", character1.item.name,\
            "which beats the weapon", character2.item.name

    elif wc_ad == character2.item:
        ch1_score -= 20
        print character2.name, "has chosen wisely the weapon: ", character2.item.name,\
            "which beats the weapon", character1.item.name

    else :
        print "Both foes are equally matched in their choice of weapons!"
    time.sleep(2)

    round_number = 0
    while ch1_score > 0 and ch2_score > 0:
        print "Round :", round_number, "has begun... FIGHT!"
        round_number += 1

        attb_choice = random.randrange(2)
        print "Attribute chosen to fight with is :", character.Character.Attributes._fields[attb_choice]

        if character1.attributes[attb_choice] > character2.attributes[attb_choice]:
            ch2_score -= 20

        elif character2.attributes[attb_choice] > character1.attributes[attb_choice]:
            ch1_score -= 20

        print character1.name, "now has a score of :", ch1_score
        print character2.name, "now has a score of :", ch2_score
        time.sleep(1)

    time.sleep(1)
    if ch1_score > ch2_score:
        print character2.name, "is vanquished!"
        time.sleep(1)
        print character1.name, "is VICTORIOUS !"
        return character1
    else:
        print character1.name, "is vanquished!"
        time.sleep(1)
        print character2.name, "is VICTORIOUS !"
        return character2


def weapon_class_advantage(item1, item2):
    outcomes = {('MeleeWeapon', 'RangedWeapon'): item2,
                ('RangedWeapon', 'MeleeWeapon'): item1,
                ('MagicalObject', 'MeleeWeapon'): item2,
                ('MeleeWeapon', 'MagicalObject'): item1,
                ('RangedWeapon', 'MagicalObject'): item2,
                ('MagicalObject', 'RangedWeapon'): item1,
                ('MeleeWeapon', 'MeleeWeapon'): None,
                ('RangedWeapon', 'RangedWeapon'): None,
                ('MagicalObject', 'MagicalObject'): None
                }

    item1_type = type(item1).__name__
    item2_type = type(item2).__name__

    wc_advantage = outcomes[(item1_type, item2_type)]
    return wc_advantage


def arena_advantage(arena, character1, character2):
    return arena.advantage
