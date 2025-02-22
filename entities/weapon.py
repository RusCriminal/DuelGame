from ursina import Entity, color, invoke, lerp
from settings import WEAPON_SCALE, WEAPON_POSITION, WEAPON_ROTATION, ATTACK_DURATION, BLOCK_DURATION

class Weapon(Entity):
    def __init__(self, parent, color=color.blue):
        super().__init__(
            model='cube',
            color=color,
            scale=WEAPON_SCALE,
            position=WEAPON_POSITION,
            parent=parent,
            rotation=WEAPON_ROTATION
        )
        self.visible = False
        self.attack_angle = 45  # Угол атаки

    def attack(self):
        self.visible = True
        self.animate_rotation((0, 0, -self.attack_angle), duration=ATTACK_DURATION)
        invoke(self.reset, delay=ATTACK_DURATION)

    def block(self):
        self.visible = True
        self.animate_rotation((0, 0, 90), duration=BLOCK_DURATION)

    def reset(self):
        self.visible = False
        self.rotation = WEAPON_ROTATION
