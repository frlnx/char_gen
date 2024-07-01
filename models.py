import dataclasses
from enum import Enum


class ActivityEnum(Enum):
    weapon_techniques = "Practicing weapon techniques"
    sneaking = "Sneaking and gathering information"
    studying = "Studying ancient tomes and practicing spells"
    rituals = "Performing rituals and healing others"
    exploring = "Exploring the wilderness and tracking creatures"


class HomeEnum(Enum):
    human_city = "A bustling human city"
    forest_village = "An enchanting forest village"
    mountains = "A stronghold carved into the mountains"
    underground = "A cozy underground burrow"
    floating_island = "A mystical, floating island or temple"
    desert_oasis = "A remote desert oasis"


class MoralDilemmaEnum(Enum):
    follow_rules = "Follow the rules and do what's right"
    do_right = "Do what feels right in the moment, regardless of rules"
    greater_good = "Weigh the situation carefully and act for the greater good"
    means_necessary = "Use whatever means necessary to achieve their goal"
    neutral = "Avoid taking sides and stay neutral"


class AdventureEnum(Enum):
    avenge_fallen = "A mission to avenge the fallen"
    protect_loved_ones = "A journey to protect loved ones from harm"
    uncover_secrets = "An expedition to uncover forgotten knowledge and secrets"
    legendary_treasures = "A venture in search of legendary treasures"
    overthrow_tyrant = "A campaign to overthrow a powerful tyrant"
    sacred_duty = "A pilgrimage to fulfill a sacred duty or prophecy"


class DemeanorEnum(Enum):
    brave_leader = "A brave leader who inspires others"
    charming_individual = "A charming individual who can talk their way out of anything"
    perceptive_intelligent = "A perceptive and intelligent individual always seeking answers"
    compassionate_healer = "A compassionate healer with a heart of gold"
    rugged_outdoorsman = "A rugged and self-sufficient outdoorsman"
    fierce_warrior = "A fierce warrior with a short temper"
    creative_artist = "A creative artist with a knack for performance"
    mystical_insightful = "A mystical and insightful person deeply connected to nature"
    disciplined_warrior = "A disciplined and honorable warrior following a strict code"
    mysterious_enigmatic = "A mysterious and enigmatic figure with a sinister edge"


@dataclasses.dataclass
class Character:
    activity: ActivityEnum
    home: HomeEnum
    moral_dilemma: MoralDilemmaEnum
    adventure: AdventureEnum
    demeanor: DemeanorEnum
