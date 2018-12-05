from string import ascii_lowercase

def react(polymer):
    length = len(polymer)
    i = 0 
    while i < length-1:
        if (polymer[i] == polymer[i+1].upper() or polymer[i] == polymer[i+1].lower()) and (polymer[i] != polymer[i+1]):
            polymer = polymer[:i] + polymer[i+2:]
            length -= 2
            i -= 2
        i += 1
    return polymer

f = open('input', 'r')
polymer = f.readline()
polymer = react(polymer)
print('Part One:')
print(f'Polymer has length {len(polymer)} after reduction.')

f.seek(0)
polymer = f.readline()
shortest_length = len(polymer)
shortest_length_unit = None
units = ascii_lowercase
for unit in units:
    unitless_polymer = polymer.replace(unit, '').replace(unit.upper(), '')
    unitless_polymer = react(unitless_polymer)
    if shortest_length > len(unitless_polymer):
        shortest_length = len(unitless_polymer)
        shortest_length_unit = unit

print('Part Two')
print(f'Shortest Polymer of length {shortest_length} after removing unit {shortest_length_unit.upper() + shortest_length_unit}.')
