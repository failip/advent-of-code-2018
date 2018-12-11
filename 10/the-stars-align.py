import numpy as np
from PIL import Image

class LightPoint:
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.position = np.array([pos_x, pos_y])
        self.velocity = np.array([vel_x, vel_y])
    
    def move_for_second(self):
        self.position += self.velocity
    
def second_passes(lights):
    for i in lights:
        lights[i].move_for_second()

def are_points_near(lights, threshold):
    points_near_eachother = 0
    for i in lights:
        point1 = lights[i]
        for j in lights:
            if i != j:
                point2 = lights[j]
                norm = np.linalg.norm(point1.position-point2.position)
                if norm == 1.0:
                    points_near_eachother += 1
                    break
        if points_near_eachother < 1:
            return False
    if points_near_eachother > threshold:
        return True      
    return False

def nightsky_to_image(lights):
    max_x = 0
    max_y = 0
    min_x = 100000
    min_y = 100000
    for i in lights:
        light = lights[i]
        pos_x = light.position[0]
        pos_y = light.position[1]
        if pos_x > max_x:
            max_x = pos_x
        if pos_x < min_x:
            min_x = pos_x
        if pos_y > max_y:
            max_y = pos_y
        if pos_y < min_y:
            min_y = pos_y
    size_x = max_x - min_x + 1
    size_y = max_y - min_y + 1
    nightsky = np.zeros((size_x, size_y), dtype=np.int8)
    for i in lights:
        light = lights[i]
        x = light.position[0] - min_x
        y = light.position[1] - min_y
        nightsky[x][y] = 254
    nightsky = np.fliplr(nightsky)
    nightsky = np.rot90(nightsky)
    Image.fromarray(nightsky, mode='L').save('nightsky.png')
    print(f'Image saved to nightsky.png.')

f = open('input', 'r')
index = 0
lights = {}

for line in f:
    splitted = line.split('<')
    pos = splitted[1]
    pos = pos.split('>')[0]
    pos = pos.split(', ')
    pos_x = int(pos[0])
    pos_y = int(pos[1])
    vel = splitted[2]
    vel = vel.split('>')[0]
    vel = vel.split(', ')
    vel_x = int(vel[0])
    vel_y = int(vel[1])
    lights[index] = LightPoint(pos_x, pos_y, vel_x, vel_y)
    index += 1

print(f'Looking at the stars waiting for the image to appear...')
threshold = int(len(lights.keys()) * 0.90)
seconds = 0
while not are_points_near(lights, threshold):
    second_passes(lights)
    seconds += 1
print(f'It took {seconds} seconds for the image to appear.')
nightsky_to_image(lights)