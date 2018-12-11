class Step:
    def __init__(self, name):
        self.name = name
        self.after = {}
        self.before = {}

class Worker:
    def __init__(self):
        self.task_time = 0
        self.task_name = None
    
    def give_task(self, task_name):
        self.task_name = task_name
        self.task_time = ord(task_name) - ord('A') + 62
    
    def work_for_second(self):
        if self.task_name:
            self.task_time -= 1
            if not self.task_time:
                step_done = self.task_name
                self.task_name = None
                return step_done

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

#topological sort: https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
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

def part_two():
    steps, first_steps = init_steps()
    time = 0
    workers = {}
    task_queue = {}
    for step in first_steps:
        worker = Worker()
        worker.give_task(step)
        workers[step] = worker
    done_tasks = [] 
    while workers:
        finished_tasks = []
        for key in workers:
            finished = workers[key].work_for_second()
            if finished:
                finished_tasks.append(finished)
                done_tasks.append(finished)
        for task in finished_tasks:
            workers.pop(task)
            finished_task = steps[task]
            for key in finished_task.after:
                can_be_added = True
                test_task = steps[key]
                for before in test_task.before:
                    can_be_added = can_be_added and (before in done_tasks)
                if can_be_added:
                    task_queue[key] = key
        while (len(workers) < 5) and task_queue:
            task_queue_keys = list(task_queue.keys())
            task_queue_keys.sort()
            task_queue_keys.reverse()
            next_task = task_queue_keys.pop()
            worker = Worker()
            worker.give_task(next_task)
            worker.work_for_second()
            workers[next_task] = worker
            task_queue.pop(next_task)
        time += 1
    print('Part Two:')
    print(f'5 Workers worked for {time-1} seconds.')
        
part_two()