from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Vec2, color
from entities.weapon import Weapon
from settings import PLAYER_SPEED, PLAYER_HEALTH, PLAYER_JUMP_HEIGHT, PLAYER_GRAVITY

class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.cursor.visible = False  # Скрыть курсор
        self.mouse_sensitivity = Vec2(40, 40)  # Чувствительность мыши
        self.gravity = PLAYER_GRAVITY
        self.jump_height = PLAYER_JUMP_HEIGHT
        self.health = PLAYER_HEALTH
        self.weapon = Weapon(parent=self)
        self.is_attacking = False
        self.is_blocking = False

    def take_damage(self, damage):
        if not self.is_blocking:
            self.health -= damage
            print(f"Игрок получил урон! Здоровье: {self.health}")
            if self.health <= 0:
                self.die()

    def die(self):
        print("Игрок побежден!")
        from ursina import application
        application.quit()
