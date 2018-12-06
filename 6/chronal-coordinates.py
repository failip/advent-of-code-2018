import numpy as np
import operator

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Map:
    def __init__(self):
        self.grid = np.zeros((360,360), dtype=(np.int8, np.int8))
        self.points = {}
        self.finite_points = {}
        self.finite_areas = {}

    def add_point(self, name, x, y):
        self.points[name] = Point(x, y)
    
    def find_finite_points(self):
        infinite_points = {} 
        for point_name in self.grid[0]:
            if not infinite_points.get(point_name):
                infinite_points[point_name] = 0
        for point_name in self.grid[359]:
            if not infinite_points.get(point_name):
                infinite_points[point_name] = 0
        for line in self.grid:
            if not infinite_points.get(line[0]):
                infinite_points[line[0]] = 0
            if not infinite_points.get(line[359]):
                infinite_points[line[359]] = 0
        for key in self.points:
            if not key in infinite_points:
                self.finite_points[key] = self.points[key]
    
    def calculate_finite_areas(self):
        for key in self.finite_points:
            self.finite_areas[key] = 0
            for x in range(len(self.grid)):
                for y in range(len(self.grid[0])):
                    if (self.grid[x][y] == key):
                        self.finite_areas[key] += 1
                               
    def fill_grid_part_one(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                closest_point = None
                closest_distance = 100000
                two_point = False
                for key in self.points:
                    point = self.points[key]
                    distance = calculate_manhatten_distance(point.x, point.y, x, y)
                    if distance < closest_distance:
                        closest_point = key
                        closest_distance = distance
                        two_point = False
                    elif distance == closest_distance:
                        two_point = True
                if two_point:
                    self.grid[x][y] = 50
                else:
                    self.grid[x][y] = closest_point
        self.find_finite_points()
        self.calculate_finite_areas()
    
    def fill_grid_part_two(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                distance_to_points = 0
                for key in self.points:
                    point = self.points[key]
                    distance_to_points += calculate_manhatten_distance(point.x, point.y, x, y)
                if distance_to_points < 10000:
                    self.grid[x][y] = 1
        

def calculate_manhatten_distance(x1, y1, x2, y2):
    return int(abs(x1 - x2) + abs(y1 - y2))


f = open('input', 'r')
m = Map()
i = 0
for line in f:
    x,y = line.split(', ')
    x = int(x)
    y = int(y)
    m.add_point(i, x, y)
    i += 1

def part_one():
    m.fill_grid_part_one()
    max_name = max(m.finite_areas.items(), key=operator.itemgetter(1))[0]
    max_area = m.finite_areas[max_name]
    print('Part One:')
    print(f'Maximum area: {max_area}')

def part_two():
    m.grid = np.zeros((360,360),dtype=(np.int8, np.int8))
    m.fill_grid_part_two()
    print('Part Two:')
    print(f'Area with distance less than 10000: {np.count_nonzero(m.grid)}')

part_one()
part_two()