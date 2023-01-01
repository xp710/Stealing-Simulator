import Rooms
import Commands
import random

if len(commands) > 2:
    enemy = Commands.findItem(player.x, player.y, commands[2])
    attack = random.randint(1, self.sides) + self.bonus
    enemy.health -= attack
    print('You attack for', attack, 'damage!')
    enemy.onHurt(enemy, player, commands)
else:
    print('Syntax: "use [weapon] [thing to attack]"')
    if Rooms.modes['devmode']:
        attack = random.randint(1, self.sides) + self.bonus
        print('You attack for', attack, 'damage!')