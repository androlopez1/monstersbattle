from monster.models import Monster

# Create your battle Algorithm here


def fight(monster_a: Monster, monster_b: Monster) -> Monster:
    turn = 1
    attacker, defender = monster_a, monster_b
    while monster_a.hp > 0 and monster_b.hp > 0:
        if turn == 1:
            if monster_b.speed > monster_a.speed:
                attacker, defender = monster_b, monster_a
            elif monster_a.speed == monster_b.speed:
                if monster_a.attack < monster_b.attack:
                    attacker, defender = monster_b, monster_a
        damage = max(attacker.attack - defender.defense, 1)
        defender.hp -= damage
        attacker, defender = defender, attacker
        turn += 1
    if monster_a.hp <= 0:
        return monster_b
    return monster_a
