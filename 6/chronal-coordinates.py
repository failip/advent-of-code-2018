import numpy as np
from shapely.geometry import Point
from shapely.geometry import Polygon
from string import ascii_lowercase
from string import ascii_uppercase

class Map:
    def __init__(self):
        self.grid = np.zeros((360,360),dtype=(np.int8,np.int8))
        self.points = {}
        self.finite_points = {}

    def add_point(self, name, x, y):
        self.points[name] = Point(x, y)
    
    def calculate_finite_points(self, name):
        point = self.points[name]
        found_triangle = False
        for key1 in self.points:
            for key2 in self.points:
                if key1 == key2:
                    pass
                for key3 in self.points:
                    if key3 == key2:
                        pass
                    first_point = self.points[key1]
                    second_point = self.points[key2]
                    third_point = self.points[key3]
                    triangle = Polygon([(first_point.x, first_point.y), 
                                        (second_point.x, second_point.y), 
                                        (third_point.x, third_point.y)])
                    if triangle.contains(point):
                        self.finite_points[name] = point
                        found_triangle = True
                        break
            if found_triangle:
                break
                                        
    def fill_grid(self):
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

print('Calculating points with finite areas...')
for key in m.points:
    print(key)
    m.calculate_finite_points(key)
print('finished\n')

print('Calculating fill grid...')
m.fill_grid()
print('finished')
np.save('./manhatten_array', m.grid)
#m.grid = np.load('./manhatten_array.npy')

finite_areas = {}
for key in m.finite_points:
    finite_areas[key] = 0
    for x in range(len(m.grid)):
        for y in range(len(m.grid[0])):
            if (m.grid[x][y] == key):
                finite_areas[key] += 1
print(finite_areas)







    

