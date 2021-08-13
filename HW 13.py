# Game
class Unit:
    def __init__(self, name='none', clan='none'):
        self.name = name
        self.clan = clan
        self.hp = 100
        self.power = 1
        self.intelligence = 1
        self.dexterity = 1

    def healing(self):
        if self.hp > 90:
            self.hp = 100
        else:
            self.hp += 10

    def up_skill(self):
        if isinstance(self, Mage) and self.intelligence < 10:
            self.intelligence += 1
        elif isinstance(self, Knight) and self.power < 10:
            self.power += 1
        elif isinstance(self, Archer) and self.dexterity < 10:
            self.dexterity += 1

class Mage(Unit):
    def __init__(self, name='none', clan='none', skill='storm'):
        super().__init__(name , clan)
        dict_skills = {'fire': 'fire',
                      'water': 'water',
                      'storm': 'storm'}
        self.skills = dict_skills[skill]

class Knight(Unit):
    def __init__(self, name='none', clan='none',weapon='axe'):
        super().__init(name, clan)
        dict_weapon = {'sword': 'sword',
                       'axe': 'axe',
                       'peak': 'peak'}
        self.weapon = dict_weapon[weapon]

class Archer(Unit):
    def __init__(self, name='none', clan='none',weapon_archer='onion'):
        super().__init__(name,clan)
        dict_weapon_archer = {'onion': 'onion',
                         'crossbow': 'crossbow'}
        self.weapon_archer = dict_weapon_archer[weapon_archer]



