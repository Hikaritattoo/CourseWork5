from assets.skills import BaseSkill


class RainbowAphidStrike(BaseSkill):
    name: str = 'Удар радужной тли'
    damage: float = 18.3
    stamina_required: float = 4.2

    def _skill_effect(self):
        self.target.health_points_ -= self.damage
        self.user.stamina_points_ -= self.stamina_required
        return f'{self.user.name} использует {self.user.unit_class.skill.name} и наносит {self.damage} урона врагу.'
