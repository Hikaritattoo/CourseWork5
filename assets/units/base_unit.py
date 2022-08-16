from __future__ import annotations
from abc import ABC

from assets.classes.unit_class import UnitClass
from assets.equipment.armor import Armor
from assets.equipment.weapon import Weapon


class BaseUnit(ABC):

    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        self.name = name
        self.unit_class = unit_class
        self.weapon = weapon
        self.armor = armor
        self.skill_used: bool = False
        self.health_points_: float = unit_class.max_health
        self.stamina_points_: float = unit_class.max_stamina

    @property
    def health_points(self):
        if self.health_points_ < 0:
            return 0
        return round(self.health_points_, 1)

    @property
    def stamina_points(self):
        return round(self.stamina_points_, 1)

    def attack(self, target: BaseUnit) -> str:
        if self.stamina_points_ >= self.weapon.stamina_per_hit:
            damage_inflicted = self._calculate_damage(target)
            target._get_damage(damage_inflicted)

            self.stamina_points_ -= self.weapon.stamina_per_hit
            target.stamina_points_ -= target.armor.stamina_per_turn

            if target.stamina_points_ < 0:
                target.stamina_points_ = 0

            if damage_inflicted > 0:
                return (f'{self.name}, использовав {self.weapon.name}, '
                        f'поражает {target.armor.name} врага и наносит {damage_inflicted} урона.')
            return (f'{self.name}, применив {self.weapon.name}, наносит удар, '
                    f' но {target.armor.name} врага его блокирует.')

        return (f'{self.name} пытался нанести {self.weapon.name},'
                f' но у него не хватило сил.')

    def use_skill(self, target: BaseUnit):
        if self.skill_used:
            return (f'{self.name} попытался использовать {self.unit_class.skill.name},'
                    f' но навык уже был использован.')
        self.skill_used = True
        return self.unit_class.skill.use(user=self, target=target)

    def _calculate_damage(self, target: BaseUnit) -> float:
        damage = self.weapon.calculate_damage() * self.unit_class.attack_modifier
        defence = target.armor.defence if target.stamina_points_ >= target.armor.stamina_per_turn else 0

        if damage < defence:
            damage_inflicted = 0
        else:
            damage_inflicted = damage - defence
        return round(damage_inflicted, 1)

    def _get_damage(self, damage_inflicted: float) -> None:
        self.health_points_ -= damage_inflicted

