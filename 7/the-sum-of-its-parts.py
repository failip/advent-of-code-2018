class Step:
    def __init__(self, name):
        self.name = name
        self.after = {}
        self.before = {}

def init_steps():
    f = open('input', 'r')
    steps = {} 
    for line in f:
        splitted = line.split(' ')
        first = splitted[1]
        second = splitted[7]
        first_step = steps.get(first)
        second_step = steps.get(second)
        if not first_step:
            first_step = Step(first)
            steps[first] = first_step
        if not second_step:
            second_step = Step(second)
            steps[second] = second_step
        steps[first].after[second] = second_step
        steps[second].before[first] = first_step

    first_steps = []
    for key in steps:
        if not steps[key].before:
            first_steps.append(key)
    f.close()
    return steps, first_steps

#topological sort https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
def part_one():
    steps, first_steps = init_steps()
    sorted_steps = []
    while first_steps:
        first_steps.sort()
        first_steps.reverse()
        step = first_steps.pop()
        sorted_steps.append(step)
        while (steps[step].after):
            after_steps = list(steps[step].after)
            after_steps.sort()
            after_steps.reverse()
            key = after_steps.pop()
            steps[step].after.pop(key)
            steps[key].before.pop(step)
            if not steps[key].before:
                first_steps.append(steps[key].name)
    print('Part One:')
    print(''.join(sorted_steps))

part_one()