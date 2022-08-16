from typing import List
import json

from assets.equipment.armor import Armor, ArmorSchema
from assets.equipment.equipment_data import EquipmentData
from assets.equipment.weapon import Weapon, WeaponSchema


class Equipment:

    def __init__(self, filename: str):
        self._filename = filename
        self.equipment: EquipmentData = self._create_equipment()

    def _create_equipment(self) -> EquipmentData:
        with open(self._filename) as file:
            data = json.load(file)
            return EquipmentData(
                weapons=WeaponSchema(many=True).load(data['weapons']),
                armor=ArmorSchema(many=True).load(data['armors']))

    def get_weapon(self, weapon_name: str) -> Weapon:
        for weapon in self.equipment.weapons:
            if weapon.name == weapon_name:
                weapon_to_equip = weapon
        return weapon_to_equip

    def get_weapon_names(self) -> List[Weapon]:
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armor(self, armor_name: str) -> Armor:
        for armor in self.equipment.armor:
            if armor.name == armor_name:
                armor_to_equip = armor
        return armor_to_equip

    def get_armor_names(self) -> List[Armor]:
        return [armor.name for armor in self.equipment.armor]

