import random
from ursina import Entity, distance, color, time, application, Vec3, lerp
from weapon import Weapon
from settings import ENEMY_SPEED, ENEMY_HEALTH, ATTACK_RANGE, ATTACK_DAMAGE

class Enemy(Entity):
    def __init__(self, target):
        super().__init__(
            model='cube',
            color=color.red,
            scale=(1, 2, 1),
            position=(10, 1, 10),
            collider='box'
        )
        self.health = ENEMY_HEALTH
        self.target = target
        self.weapon = Weapon(parent=self, color=color.magenta)
        self.is_attacking = False
        self.dodge_chance = 0.3  # Шанс уклонения

    def update(self):
        self.move_towards_target()
        self.attack_target()
        self.check_health()

    def move_towards_target(self):
        self.look_at(self.target.position)
        self.position += self.forward * time.dt * ENEMY_SPEED

    def attack_target(self):
        if distance(self, self.target) < ATTACK_RANGE and not self.is_attacking:
            self.is_attacking = True
            self.weapon.attack()
            invoke(self.weapon.reset, delay=0.2)
            if random.random() > self.dodge_chance:  # Игрок может уклониться
                self.target.take_damage(ATTACK_DAMAGE)
            self.is_attacking = False

    def take_damage(self, damage):
        self.health -= damage
        print(f"Враг получил урон! Здоровье врага: {self.health}")

    def check_health(self):
        if self.health <= 0:
            print("Враг побежден!")
            application.quit()
