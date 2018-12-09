class Marble:
    def __init__(self, value):
        self.value = value
        self.next_clockwise = None
        self.next_counter_clockwise = None

class Player:
    def __init__(self):
        self.marbles = []
        self.score = 0
    
    def take_marble(self, marble):
        self.marbles.append(marble)
        self.score += marble.value

class Marble_Game:
    def __init__(self, number_of_players, number_of_marbles):
        self.current_player = 0
        self.number_of_players = number_of_players
        self.players = {}
        for i in range(number_of_players):
            self.players[i] = Player()
        self.number_of_marbles = number_of_marbles + 1
        self.current_marble = None

    def play_round(self, round_number):
        self.current_player += 1
        marble = Marble(round_number)
        if self.number_of_players <= self.current_player:
            self.current_player -= self.number_of_players
        #first_round
        if round_number == 0:
            marble.next_clockwise = marble
            marble.next_counter_clockwise = marble
            self.current_marble = marble
        #all_other_rounds
        elif round_number % 23 == 0:
            for i in range(7):
                self.current_marble = self.current_marble.next_counter_clockwise
            next_marble = self.current_marble.next_clockwise
            previous_marble = self.current_marble.next_counter_clockwise
            next_marble.next_counter_clockwise = previous_marble
            previous_marble.next_clockwise = next_marble
            self.players[self.current_player].take_marble(marble)
            self.players[self.current_player].take_marble(self.current_marble)
            self.current_marble = next_marble
        else:
            next_marble = self.current_marble.next_clockwise
            next_next_marble = next_marble.next_clockwise
            next_marble.next_clockwise = marble
            next_next_marble.next_counter_clockwise = marble
            marble.next_counter_clockwise = next_marble
            marble.next_clockwise = next_next_marble
            self.current_marble = marble
                           
    def play(self):
        for i in range(self.number_of_marbles):
            self.play_round(i)
        player_scores = []
        for i in range(self.number_of_players):
            player_scores.append(self.players[i].score)
        print(f'Max score is: {max(player_scores)}')
        
f = open('input', 'r')
line = f.readline()
splitted = line.split()
number_of_players = int(splitted[0])
number_of_marbles_round_one = int(splitted[6])
number_of_marbles_round_two = number_of_marbles_round_one * 100
print('Part One:')
print(f'Playing game with {number_of_marbles_round_one} marbles.')
game = Marble_Game(number_of_players, number_of_marbles_round_one)
game.play()
print('Part Two:')
print(f'Playing game with {number_of_marbles_round_two} marbles.')
game = Marble_Game(number_of_players, number_of_marbles_round_two)
game.play()