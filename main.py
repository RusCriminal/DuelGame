from ursina import Ursina, time
from entities.player import Player
from entities.enemy import Enemy
from systems.input_system import handle_input

def main():
    app = Ursina()

    # Создание игрока и противника
    player = Player()
    enemy = Enemy(target=player)

    # Основной игровой цикл
    def update():
        handle_input(player, enemy)
        enemy.update()

    app.run()

if __name__ == "__main__":
    main()
