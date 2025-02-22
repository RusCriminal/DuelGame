mport random

def handle_combat(attacker, target, damage, dodge_chance):
    if random.random() > dodge_chance:  # Проверка на уклонение
        target.take_damage(damage)
