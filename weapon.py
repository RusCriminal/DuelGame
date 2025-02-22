from ursina import Entity, color, invoke

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
        self.attack_angle = 45  # Угол атаки

    def attack(self):
        self.visible = True
        self.animate_rotation((0, 0, -self.attack_angle), duration=0.1)  # Анимация атаки
        invoke(self.reset, delay=0.2)

    def block(self):
        self.visible = True
        self.animate_rotation((0, 0, 90), duration=0.1)  # Анимация блокировки

    def reset(self):
        self.visible = False
        self.rotation = (0, 0, 45)  # Возврат в исходное положение
