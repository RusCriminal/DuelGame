from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import held_keys, distance, invoke, time, color, application, Vec2
from weapon import Weapon
from settings import PLAYER_SPEED, PLAYER_HEALTH, ATTACK_RANGE, ATTACK_DAMAGE

class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.cursor.visible = False  # Скрыть курсор
        self.mouse_sensitivity = Vec2(40, 40)  # Чувствительность мыши
        self.gravity = 0.5
        self.jump_height = 1
        self.health = PLAYER_HEALTH
        self.weapon = Weapon(parent=self)
        self.is_attacking = False
        self.is_blocking = False

    def update(self):
        self.move()
        self.check_health()

    def move(self):
        if held_keys['w']:
            self.position += self.forward * time.dt * PLAYER_SPEED
        if held_keys['s']:
            self.position += self.back * time.dt * PLAYER_SPEED
        if held_keys['a']:
            self.position += self.left * time.dt * PLAYER_SPEED
        if held_keys['d']:
            self.position += self.right * time.dt * PLAYER_SPEED

    def attack(self, target):
        if not self.is_attacking:
            self.is_attacking = True
            self.weapon.attack()
            invoke(self.weapon.reset, delay=0.2)
            if distance(self, target) < ATTACK_RANGE:
                target.take_damage(ATTACK_DAMAGE)
            self.is_attacking = False

    def block(self):
        self.is_blocking = True
        self.weapon.color = color.gray

    def stop_block(self):
        self.is_blocking = False
        self.weapon.color = color.blue

    def take_damage(self, damage):
        if not self.is_blocking:
            self.health -= damage
            print(f"Игрок получил урон! Здоровье: {self.health}")

    def check_health(self):
        if self.health <= 0:
            print("Игрок побежден!")
            application.quit()
