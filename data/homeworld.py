from stats import *
from .background import Background


class Homeworld:
    modifiers:dict[CharName, int]
    fate:int
    bless:int
    bonus:str
    aptitude:AptitudeName
    wounds:int
    backgrounds:list[Background]


    def give(character):
        pass