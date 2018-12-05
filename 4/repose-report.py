from subprocess import call
import numpy as np

class Guard:
    sleep = 0
    def __init__(self, ID):
        self.ID = ID
        self.minutes_slept = 0
        self.most_slept_minute = 0
        self.minutes = np.zeros(60)

    def fall_asleep(self, time):
        self.sleep = time
    
    def wake_up(self, time):
        for i in range(self.sleep, time):
            self.minutes_slept += 1
            self.minutes[i] += 1
        self.most_slept_minute = self.minutes.max()

call("sort input -o sorted", shell = True) 
open('sorted','r')
f = open('sorted', 'r')
guards = {}
for line in f:
    if 'Guard' in line:
        splitted = line.split(' ')
        ID = int(splitted[3][1:])
        guard = guards.get(ID)
        if(not guard):
            guard = Guard(ID)
            guards[ID] = guard
    else:
        splitted = line.split(' ')
        time = int(splitted[1][3:][:-1])
        if 'falls' in line:
            guard.fall_asleep(time)
        else:
            guard.wake_up(time)

max_time_asleep = 0
guard_longest_asleep = None
for key in guards:
    guard = guards[key]
    if guard.minutes_slept > max_time_asleep:
        max_time_asleep = guard.minutes_slept
        guard_longest_asleep = guard

print('Strategy 1:')
print(f'Guard #{guard_longest_asleep.ID} was asleep for {guard_longest_asleep.minutes_slept} Minutes.')
print(f'Most time asleep at Minute {guard_longest_asleep.minutes.argmax()}.')
print(f'Solution: {guard_longest_asleep.minutes.argmax() * guard_longest_asleep.ID}')
    
max_time_asleep = 0
guard_longest_asleep = None
for key in guards:
    guard = guards[key]
    if guard.most_slept_minute > max_time_asleep:
        max_time_asleep = guard.most_slept_minute
        guard_longest_asleep = guard

print('\nStrategy 2:')
print(f'Guard #{guard_longest_asleep.ID} was asleep for {int(guard_longest_asleep.most_slept_minute)} Minutes on Minute {guard_longest_asleep.minutes.argmax()}.')
print(f'Solution: {guard_longest_asleep.minutes.argmax() * guard_longest_asleep.ID}')


    
    



