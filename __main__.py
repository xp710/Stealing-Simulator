import Rooms
import Commands

def npcOnHurt(self, player, commands):
    script = Commands.setUpScript(self.scripts['onHurt'])
    if script != False:
        exec(script)

def getHealth(player, commands):
    print('Health:',player.health)

Rooms.inputs['health'] = (getHealth, 'Type "health" to check your health.')

Rooms.roomlist = [[0 for i in range(50)] for j in range(50)]
Rooms.itemlist = [[[] for i in range(50)] for j in range(50)]
player = Rooms.Player(0, 0)
player.health = 30

# Bedroom
Rooms.roomlist[0][0] = Rooms.Room('Bedroom', "This is your bedroom. It's filled to the\n"
                                             "brim with stolen objects, like traffic cones\n"
                                             "and manhole covers.\n"
                                             "To the east is the living room.", {}, {}, {})
hoodie = Rooms.Item('big hoodie', 'A big, black hoodie, good for\n'
                                  'hiding stuff under.', {}, {})
key = Rooms.Key('house key', 'This goes to the front door.', [{'x': 1, 'y': 0, 'dir': 'e'}], {})
closet = Rooms.Item('closet', 'A closet built into the walls of your house. You\n'
                              'can\'t walk inside, but it\'s big enough\n'
                              'for all your stuff.', {'useable':True, 'takeable':False}, {'use':'steal/scripts/chest.py'})
closet.items = [hoodie, key]
Rooms.itemlist[0][0].append(closet)
Rooms.itemlist[0][0].append(Rooms.Item('paper', 'type "use closet" to look inside it!\n'
                                                'type "use closet [item]" to get an item out of the closet!', {}, {}))

# Living Room
Rooms.roomlist[1][0] = Rooms.Room('Living Room', "Your living room is a lot cleaner than your\n"
                                                 "bedroom, all there really is is a tv and a sofa.\n"
                                                 "The bedroom is to the west.\n"
                                                 "The kitchen is to the north.\n"
                                                 "The front door is to the east.",
                                  {'e':True}, {}, {})

# Kitchen
Rooms.roomlist[1][1] = Rooms.Room('Kitchen', 'Your kitchen is indescribably filthy.\n'
                                             'The living room is to the south.',
                                  {}, {}, {})
pan = Rooms.Item('pan', 'A cast iron pan, great for hitting people.', {'useable':True}, {'use':'steal/scripts/weapon.py'})
pan.picture = 'steal/pictures/pan.txt'
pan.sides = 4
pan.bonus = 4
cupboard = Rooms.Item('cupboard', 'A wooden cupboard.', {'useable':True, 'takeable':False}, {'use':'steal/scripts/chest.py'})
cupboard.items = [pan, Rooms.Item('$10', 'A ten dollar bill, crumpled and torn.', {}, {})]
Rooms.itemlist[1][1].append(cupboard)

# Driveway
Rooms.roomlist[2][0] = Rooms.Room('Driveway', "It's a beautiful sunny day out today!", {}, {}, {})
Rooms.itemlist[2][0].append(Rooms.Teleporter('car', 'Your grey Ford Taurus SE (2005)', {'takeable':False}, [5, 5], {}))

# Parking Lot
Rooms.roomlist[5][5] = Rooms.Room('Parking Lot', 'The store entrance is to the north.', {}, {}, {})
Rooms.itemlist[5][5].append(Rooms.Teleporter('car', 'Your grey Ford Taurus SE (2005)', {'takeable':False}, [2, 0], {}))

# Store
Rooms.roomlist[5][6] = Rooms.Room('Store', "This is a tiny little convenience store.", {}, {}, {'onExit':'steal/scripts/Store_onExit.py'})
shelf = Rooms.Item('shelf', 'A flimsy, white shelf.', {'useable':True, 'takeable':False}, {'use':'steal/scripts/chest.py'})
shelf.items = [Rooms.Item('chips', 'A bag of chips', {}, {})]
shelf.numItems = len(shelf.items)
Rooms.itemlist[5][6].append(shelf)
brassKnuckles = Rooms.Item('brass knuckles', 'A bloody piece of deadly metal.', {'useable':True}, {'use':'steal/scripts/weapon.py'})
brassKnuckles.sides = 10
brassKnuckles.bonus = 5
shopkeep = Rooms.Item('shopkeep', 'A small, happy looking man.', {}, {'use':'steal/scripts/npc.py', 'onHurt':'steal/scripts/npc_onHurt.py'})
shopkeep.onHurt = npcOnHurt
shopkeep.health = 15
shopkeep.hostile = False
shopkeep.weapon = brassKnuckles
Rooms.itemlist[5][6].append(shopkeep)
Rooms.gameLoopFunctions.append(shopkeep.use)

Commands.look(player, ['look'])
Rooms.roomlist[0][0].entered = True
Rooms.gameLoop(player)