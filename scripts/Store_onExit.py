import Rooms
import Commands

shelf = Commands.findItem(5, 6, 'shelf')
shopkeep = Commands.findItem(5, 6, 'shopkeep')
concealed = False

if len(shelf.items) < shelf.numItems:
    for i in player.inventory:
        if 'hoodie' in i.name:
            concealed = True
    if not Commands.findItem(5, 6, '$10') and not concealed:
        shopkeep.hostile = True
        print('The shopkeep follows you out, stealer!')
        Rooms.itemlist[5][6].remove(shopkeep)
        Rooms.itemlist[5][5].append(shopkeep)