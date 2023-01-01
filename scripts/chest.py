if len(commands) > 2:
    itemName = commands[2]
    for i in self.items:
        if itemName in i.name.lower():
            print('You got:', i.name)
            player.inventory.append(i)
            self.items.remove(i)
else:
    print('Contains:')
    for i in self.items:
        print(i.name)