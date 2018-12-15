from collections import defaultdict

class Cart:
    def __init__(self, pos_x, pos_y, symbol):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dir_x, self.dir_y = self.get_direction(symbol)
        self.next_intersection = 0
        self.moved = False
    
    def get_direction(self, symbol):
        if symbol == '<':
            return -1, 0
        if symbol == '>':
            return 1, 0
        if symbol == 'v':
            return 0, 1
        if symbol == '^':
            return 0, -1
    
    def turn_left(self):
        if self.dir_x:
            self.dir_y = -self.dir_x
            self.dir_x = 0
        else:
            self.dir_x = self.dir_y
            self.dir_y = 0
    
    def turn_right(self):
        if self.dir_x:
            self.dir_y = self.dir_x
            self.dir_x = 0
        else:
            self.dir_x = -self.dir_y
            self.dir_y = 0

    def handle_intersection(self):
        if self.next_intersection == 0:
            self.turn_left()
            self.next_intersection += 1
        elif self.next_intersection == 1:
            self.next_intersection += 1
        else:
            self.turn_right()
            self.next_intersection = 0


class Track:
    def __init__(self, symbol):
        self.symbol = symbol
        self.cart_on_track = None

    def arrive_on(self, cart):
        if self.symbol == '+':
            cart.handle_intersection()
        elif self.symbol == '/':
            if cart.dir_x == 0:
                cart.turn_right()
            else:
                cart.turn_left()
        elif self.symbol == '\\':
            if cart.dir_y == 0:
                cart.turn_right()
            else:
                cart.turn_left()
        self.cart_on_track = cart
    
    def cart_leaves(self):
        self.cart_on_track = None


def is_cart(track):
    if track in ['<', '>']:
        return '-'
    elif track in ['v', '^']:
        return '|'

f = open('input', 'r')
tracks = defaultdict(dict)
carts = defaultdict(dict)
cart_index = 0
x = 0
y = 0
for line in f:
    splitted = list(line)
    for track in splitted:
        track_symbol = is_cart(track)
        if track_symbol:
            cart = Cart(x, y, track)
            carts[cart_index] = cart
            cart_index += 1
            tracks[x][y] = Track(track_symbol)
            tracks[x][y].arrive_on(cart)
        else:
            tracks[x][y] = Track(track)
        x += 1
    x = 0
    y += 1

crashed = False
while not (len(carts.keys()) == 1):
    for x in tracks:
        for y in tracks[0]:
            track = tracks[x][y]
            cart = track.cart_on_track
            if cart and not cart.moved:
                cart.moved = True
                dir_x = cart.dir_x
                dir_y = cart.dir_y
                tracks[x][y].cart_leaves()
                next_track = tracks[x+dir_x][y+dir_y]
                next_cart = next_track.cart_on_track
                if next_cart:
                    print(f'Crashed on tile {x+dir_x},{y+dir_y}')
                    k1 = 0
                    k2 = 0
                    for k in carts:
                        if carts[k] == cart:
                            k1 = k
                        if carts[k] == next_cart:
                            k2 = k
                    print('Deleted',k1,k2)
                    del carts[k1]
                    del carts[k2]
                    next_track.cart_leaves()
                else:
                    next_track.arrive_on(cart)
    for k in carts:
        carts[k].moved = False

for x in tracks:
    for y in tracks[0]:
        track = tracks[x][y]
        cart = track.cart_on_track
        if cart:
            print(x,y)
            
#very messy will clean up