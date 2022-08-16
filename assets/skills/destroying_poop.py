from assets.skills import BaseSkill


class DestroyingPoop(BaseSkill):
    name: str = 'Пинок клеща'
    damage: float = 15.5
    stamina_required: float = 5.8

    def _skill_effect(self):
        self.target.health_points_ -= self.damage
        self.user.stamina_points_ -= self.stamina_required
        return f'{self.user.name} использует {self.user.unit_class.skill.name} и наносит {self.damage} урона врагу.'


