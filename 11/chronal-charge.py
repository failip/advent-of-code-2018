import numpy as np

def create_grid(serial_number):
    grid = np.zeros((300,300), dtype=np.int8)
    for x in range(300):
        for y in range(300):
            ID = x + 1 + 10
            power_level = ID * (y + 1)
            power_level += serial_number
            power_level *= ID
            power_level = power_level // 100 % 10
            power_level -= 5
            grid[x,y] = power_level
    grid = np.fliplr(grid)
    grid = np.rot90(grid)

    return grid

def get_largest_fuel_cell(grid, size):
    left_corner = None
    max_fuel_charge = 0
    max_subgrid = None
    for x in range(300 - size):
        for y in range(300 - size):
            subgrid = grid[x:x+size,y:y+size]
            fuel_charge = np.sum(subgrid)  
            if fuel_charge > max_fuel_charge:
                max_subgrid = subgrid
                left_corner = [y + 1, x + 1]
                max_fuel_charge = fuel_charge
    return left_corner, max_fuel_charge



serial_number = int(open('input', 'r').readline())
grid = create_grid(serial_number)
left_corner, fuel_charge = get_largest_fuel_cell(grid, 3)
print('Part One:')
print(f'Left corner of largest fuel cell: {left_corner[0]},{left_corner[1]}')


fuel_charges = np.zeros(300)
left_corners = [None] * 300
for i in range(300):
    left_corners[i], fuel_charges[i] = get_largest_fuel_cell(grid, i+1)

max_index = np.argmax(fuel_charges)
print('Part Two:')
print(f'Left corner of largest fuel cell with size: {left_corners[max_index][0]},{left_corners[max_index][1]},{max_index+1}')    