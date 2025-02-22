import random
from ursina import Entity, distance, color, time, Vec3
from entities.weapon import Weapon
from settings import ENEMY_SPEED, ENEMY_HEALTH, ENEMY_DODGE_CHANCE, ATTACK_RANGE, ATTACK_DAMAGE

class Enemy(Entity):
    def __init__(self, target):
        super().__init__(
            model='cube',  # Модель врага
            color=color.red,  # Цвет врага
            scale=(1, 2, 1),  # Масштаб врага
            position=(5, 1, 5),  # Позиция врага
            collider='box'  # Коллайдер для взаимодействий
        )
        self.health = ENEMY_HEALTH
        self.target = target
        self.weapon = Weapon(parent=self, color=color.magenta)
        self.is_attacking = False
        self.dodge_chance = ENEMY_DODGE_CHANCE

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
            if random.random() > self.dodge_chance:  # Игрок может уклониться
                self.target.take_damage(ATTACK_DAMAGE)
            self.is_attacking = False

    def take_damage(self, damage):
        self.health -= damage
        print(f"Враг получил урон! Здоровье врага: {self.health}")
        if self.health <= 0:
            self.die()

    def check_health(self):
        if self.health <= 0:
            self.die()

    def die(self):
        print("Враг побежден!")
        from ursina import application
        application.quit()
