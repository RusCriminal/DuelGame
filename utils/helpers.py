from ursina import distance

def is_within_range(attacker, target, range):
    return distance(attacker.position, target.position) <= range
