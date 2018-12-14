f = open('input', 'r')
first_line = f.readline()
initial_state = first_line.split()[2]
f.readline()
rules = {}
for rule in f:
    key, arrow, plant = rule.split()
    rules[key] = plant

def part_one(state, generations):
    initial_pot = 0
    for generation in range(generations):
        length = len(state)
        if not state[0:5] == '.....':
            state = '....' + state
            length += 5
            initial_pot += 4
        if not state[length-5:length] == '.....':
            state = state + '.....'
            length += 5
        next_gen = ['.'] * length
        for i in range(2,len(state)-3):
            key = state[i-2:i+3]
            plant = rules.get(key)
            if plant:
                next_gen[i] = plant
        state = ''.join(next_gen)
    sum_of_plants = 0
    for i in range(len(state)):
        if state[i] == '#':
            sum_of_plants += i - initial_pot
    return state, sum_of_plants

generations = 20
state, sum_of_plants = part_one(initial_state, generations)
print('Part One:')
print(f'Sum of plant numbers after {generations} generations: {sum_of_plants}')
