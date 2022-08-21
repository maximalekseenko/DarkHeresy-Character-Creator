from ..homeworld import Homeworld
from stats import *



class FeralWorld(Homeworld):
    name = "Feral World"
    modifiers = {
        CharName.STRENGTH: 1,
        CharName.TOUGHNESS: 1,
        CharName.INFLUENCE: -1}
    fate = 2
    bless = 3
    bonus = "The Old Ways: In the hands of a feral world character, any Low-Tech weapon loses the Primitive quality (if it had it) and gains the Proven (3) quality."
    aptitude = AptitudeName.TOUGHNESS
    wounds = 9
    backgrounds:list