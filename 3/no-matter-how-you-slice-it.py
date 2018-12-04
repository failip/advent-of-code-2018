import numpy as np

class Fabric:
    spaces = np.zeros((1000, 1000))

    def claim(self, x,y,size_x,size_y):
        for i in range(size_x):
            for j in range(size_y):
                self.spaces[x+i][y+j] += 1
    
    def count_not_ones(self):
        count = 0
        for i in range(1000):
            for j in range(1000):
                if self.spaces[i][j] > 1:
                    count += 1
        return count

    def is_intact(self, x,y,size_x,size_y):
        intact = True
        for i in range(size_x):
            for j in range(size_y):
                intact = intact and (self.spaces[x+i][y+j] == 1)
        return intact
    

def fill_the_cloth():
    f = open('input', 'r')
    fabric = Fabric()
    for line in f:
        splitted = line.split(" ")
        x,y = splitted[2].split(",")
        x = int(x)
        y = int(y[:-1])
        x_size, y_size = splitted[3].split("x")
        x_size = int(x_size)
        y_size = int(y_size)
        fabric.claim(x,y,x_size,y_size)
    print(fabric.count_not_ones())
    f.seek(0)
    for line in f:
        splitted = line.split(" ")
        x,y = splitted[2].split(",")
        x = int(x)
        y = int(y[:-1])
        x_size, y_size = splitted[3].split("x")
        x_size = int(x_size)
        y_size = int(y_size)
        if(fabric.is_intact(x,y,x_size,y_size)):
            print(splitted[0])
    f.close()

fill_the_cloth()