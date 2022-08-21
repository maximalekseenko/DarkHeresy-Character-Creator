from enum import Enum



class CharName(Enum):
    WEAPON_SKILL = 0
    BALLISTIC_SKILL = 1
    STRENGTH = 2
    TOUGHNESS = 3
    AGILITY = 4

    INTELLIGENCE = 5
    PERCEPTION = 6
    WILLPOWER  = 7
    FELLOWSHIP = 8
    INFLUENCE = 9

    WS = 0
    BS = 1
    S = 2
    T = 3
    AG = 4

    INT = 5
    PER = 6
    WP  = 7
    FEL = 8
    INF = 9



class Char:
    def __init__(self, name:CharName, value=None, modifier=0) -> None:
        '''arguments:
        \n `name`: name of this characteristic.
        \n `value`: default value; if None, will generated randomly.
        \n `modifier`: modifier for generate function.
        '''
        self.name = name
        self.value = value
        self.modifier = modifier


        if value == None: self.Gen()


    @property
    def mod(self):
        return self.value // 10

    
    def Gen(self):
        '''Generate value for this characteristic.
        \n If `modifier` is equal to zero, two rolls will be made.
        \n If `modifier` is more than zero, two best rolls out of three will be taken;
        \n If `modifier` is less than zero, two worst rolls out of three will be taken;
        '''
        from random import randint

        # roll dices
        rolls = [randint(1,10), randint(1,10), randint(1,10)]
        
        # set value to sum of dices with modifier
        if  self.modifier == 0: self.value = sum(rolls[:2])
        elif self.modifier < 0: self.value = sum(sorted(rolls)[:2])
        elif self.modifier > 0: self.value = sum(sorted(rolls, reverse=True)[:2])

        # add 20
        self.value += 20


    def __repr__(self) -> str:
        return f"{self.name}: {self.value}"
