from ursina import invoke, lerp

def animate_attack(weapon, target, damage):
    weapon.visible = True
    weapon.animate_rotation((0, 0, -weapon.attack_angle), duration=0.1)
    invoke(weapon.reset, delay=0.2)
    if distance(weapon.parent, target) < weapon.attack_range:
        target.take_damage(damage)

def animate_block(weapon):
    weapon.visible = True
    weapon.animate_rotation((0, 0, 90), duration=0.1)
