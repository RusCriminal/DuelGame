from ursina import Ursina, time
from entities import Player, Enemy
from systems import handle_input
from utils import is_within_range
from settings import ATTACK_RANGE, ATTACK_DAMAGE, ENEMY_DODGE_CHANCE

def main():
    app = Ursina()

    # Создание игрока и противника
    player = Player()
    enemy = Enemy(target=player)

    # Отладочный вывод
    print("Игрок создан:", player)
    print("Враг создан:", enemy)

    # Основной игровой цикл
    def update():
        handle_input(player, enemy)
        enemy.update()

        # Проверка боя
        if is_within_range(player, enemy, ATTACK_RANGE):
            handle_combat(player, enemy, ATTACK_DAMAGE, ENEMY_DODGE_CHANCE)

    app.run()

if __name__ == "__main__":
    main()
