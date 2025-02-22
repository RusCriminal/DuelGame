# weapon.py

from ursina import Entity, color

class Weapon(Entity):
    def __init__(self, parent, color=color.blue):
        super().__init__(
            model='cube',
            color=color,
            scale=(0.5, 0.5, 2),
            position=(0.5, -0.5, 1),
            parent=parent,
            rotation=(0, 0, 45)
        )
        self.visible = False

    def attack(self):
        self.visible = True

    def reset(self):
        self.visible = False
