from ..homeworld import Homeworld
from stats import *



class HiveWorld(Homeworld):
    name = "Hive World"
    modifiers = {
        CharName.AGILITY: 1,
        CharName.PERCEPTION: 1,
        CharName.WILLPOWER: -1}
    fate = 2
    bless = 6
    bonus = "Teeming Masses in Metal Mountains: A hive world character ignores crowds for purposes of movement, treating them as open terrain. When in enclosed spaces, he also gains a +20 bonus to Navigate (Surface) tests."
    aptitude = AptitudeName.PERCEPTION
    wounds = 8
    backgrounds:list