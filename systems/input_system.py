from ursina import held_keys, mouse

def handle_input(player, enemy):
    if held_keys['w']:
        player.position += player.forward * player.speed * time.dt
    if held_keys['s']:
        player.position += player.back * player.speed * time.dt
    if held_keys['a']:
        player.position += player.left * player.speed * time.dt
    if held_keys['d']:
        player.position += player.right * player.speed * time.dt

    if mouse.left:
        player.attack(enemy)
    if mouse.right:
        player.block()
