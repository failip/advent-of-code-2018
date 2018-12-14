def part_one(state, generations, rules):
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
    print(initial_pot)
    for i in range(len(state)):
        if state[i] == '#':
            sum_of_plants += i - initial_pot
    return state, sum_of_plants

def count_plants(state, offset=0):
    sum_of_plants = 0
    for i in range(len(state)):
        if state[i] == '#':
            sum_of_plants += i + offset
    return sum_of_plants

def let_plants_grow(state, generations, rules):
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
    return state, initial_pot

f = open('input', 'r')
first_line = f.readline()
initial_state = first_line.split()[2]
f.readline()
rules = {}
for rule in f:
    key, arrow, plant = rule.split()
    rules[key] = plant

generations = 20
state, initial_pot = let_plants_grow(initial_state, generations, rules)
sum_of_plants = count_plants(state, -initial_pot)
print('Part One:')
print(f'Sum of plant numbers after {generations} generations: {sum_of_plants}')

#Part two 2 looked at the output of the first 1000 generations found repeating pattern after 184 generations
generations = 184
state, initial_pot = let_plants_grow(initial_state, generations, rules)
sum_of_plants = count_plants(state, 50000000000 - 184 - initial_pot)
generations = 50000000000
print('Part Two:')
print(f'Sum of plant numbers after {generations} generations: {sum_of_plants}')