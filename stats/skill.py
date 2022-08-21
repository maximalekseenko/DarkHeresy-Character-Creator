from enum import Enum
from .char import CharName



class SkillName(Enum):
    PARRY = 0
    
    ATHLETICS  = 1
    INTIMIDATE = 2

    ACROBATICS          = 10
    DODGE               = 11
    OPERATE_AERONAUTICA = 12
    OPERATE_SURFACE     = 13
    OPERATE_VOIDSHIP    = 14
    SLEIGHT_OF_HAND     = 15
    STEALTH             = 16

    COMMERCE         = 20
    LOGIC            = 21
    MEDICAE          = 22
    NAVIGATE_SURFACE = 23
    NAVIGATE_STELLAR = 24
    NAVIGATE_WARP    = 25
    SECURITY         = 26
    TECH_USE         = 27

    AWARENESS    = 30
    PSYNISCIENCE = 31
    SCRUTINY     = 32
    SURVIVAL     = 33

    INTERROGATION = 40

    CHARM   = 50
    COMMAND = 51
    DECEIVE = 52
    INQUIRY = 53

    # TODO write lores
    COMMON_LORE      = 60

    FORBIDDEN_LORE   = 70

    LINGUISTICS      = 80

    SCHOLASTIC_LORE  = 90

    TRADE            = 100



class SkillChar(Enum):
    SkillName.PARRY = CharName.WS
    
    SkillName.ATHLETICS  = CharName.S
    SkillName.INTIMIDATE = CharName.S

    SkillName.ACROBATICS          = CharName.AG
    SkillName.DODGE               = CharName.AG
    SkillName.OPERATE_AERONAUTICA = CharName.AG
    SkillName.OPERATE_SURFACE     = CharName.AG
    SkillName.OPERATE_VOIDSHIP    = CharName.AG
    SkillName.SLEIGHT_OF_HAND     = CharName.AG
    SkillName.STEALTH             = CharName.AG

    SkillName.COMMERCE         = CharName.INT
    SkillName.LOGIC            = CharName.INT
    SkillName.MEDICAE          = CharName.INT
    SkillName.NAVIGATE_SURFACE = CharName.INT
    SkillName.NAVIGATE_STELLAR = CharName.INT
    SkillName.NAVIGATE_WARP    = CharName.INT
    SkillName.SECURITY         = CharName.INT
    SkillName.TECH_USE         = CharName.INT

    SkillName.AWARENESS    = CharName.PER
    SkillName.PSYNISCIENCE = CharName.PER
    SkillName.SCRUTINY     = CharName.PER
    SkillName.SURVIVAL     = CharName.PER

    SkillName.INTERROGATION = CharName.WP

    SkillName.CHARM   = CharName.FEL
    SkillName.COMMAND = CharName.FEL
    SkillName.DECEIVE = CharName.FEL
    SkillName.INQUIRY = CharName.FEL

    # TODO write lores
    SkillName.COMMON_LORE      = CharName.INT

    SkillName.FORBIDDEN_LORE   = CharName.INT

    SkillName.LINGUISTICS      = CharName.INT

    SkillName.SCHOLASTIC_LORE  = CharName.INT

    SkillName.TRADE            = CharName.INT



class Skill:
    def __init__(self, name:SkillName, level=0) -> None:
        '''arguments:
        \n `name`: name of this characteristic.
        \n `level`: level of skill from Known to +30.
        '''
        self.name = name
        self.level = level


    def __repr__(self) -> str:
        return f"{self.name}: {self.value}"
