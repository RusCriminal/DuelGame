# main.py

from ursina import Ursina, held_keys, mouse
from player import Player
from enemy import Enemy

app = Ursina()

# Создание игрока и противника
player = Player()
enemy = Enemy(target=player)

# Обработка ввода игрока
def input(key):
    if key == 'left mouse down':
        player.attack(enemy)
    if key == 'right mouse down':
        player.block()
    if key == 'right mouse up':
        player.stop_block()

# Запуск игры
app.run()
