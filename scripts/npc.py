import Rooms
import Commands
import random

if self.hostile:
    if Commands.findItem(player.x, player.y, self.name) != False and self.health > 0:
        attack = random.randint(1, self.weapon.sides) + self.weapon.bonus
        player.health -= attack
        print(self.name, 'attacks you for', attack, 'damage!')
        if player.health <= 0:
            print('You died!')
            exit()