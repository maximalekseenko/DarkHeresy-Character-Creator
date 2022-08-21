from stats import *
from stats.skill import SkillName



class Background:
    name:str
    starting_skills:list[SkillName]
    starting_talents:list
    starting_equipment:None
    background_bonus:str
    background_atitudes:list[AptitudeName]
    recommended_roles:list