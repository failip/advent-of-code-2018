import numpy as np
from shapely.geometry import Point
from shapely.geometry import Polygon
from string import ascii_lowercase
from string import ascii_uppercase

class Map:
    def __init__(self):
        self.grid = np.zeros((360,360))
        self.points = {}
        self.finite_points = {}

    def add_point(self, name, x, y):
        self.points[name] = Point(x, y)
    
    def calculate_finite_points(self, name):
        point = self.points[name]
        first_point = None
        second_point = None
        third_point = None
        for key in self.points:
            if key != name:
                if not first_point:
                    first_point = self.points[key]
                elif not second_point:
                    second_point = self.points[key]
                elif not third_point:
                    third_point = self.points[key]
                else:
                    third_point = second_point
                    second_point = first_point
                    first_point = self.points[key]
                    triangle = Polygon([(first_point.x, first_point.y), 
                                        (second_point.x, second_point.y), 
                                        (third_point.x, third_point.y)])
                    if triangle.contains(point):
                        self.finite_points[name] = point
                        break

    def fill_grid(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                print(x,y)
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
                    self.grid[x][y] = 80
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

for key in m.points:
    m.calculate_finite_points(key)
m.fill_grid()
np.save('./manhatten_array', m.grid)




    

