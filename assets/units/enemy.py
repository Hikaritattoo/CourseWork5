from random import randint
from assets.units.base_unit import BaseUnit


class Enemy(BaseUnit):
    def attack(self, target: BaseUnit) -> str:
        if not self.skill_used:
            use_skill = randint(0, 9)
            if use_skill == 0:
                return self.use_skill(target)

        return super().attack(target)