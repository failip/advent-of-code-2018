def part_one():
    f = open('input', 'r')
    s = 0
    for num in f:
        s += int(num)
    f.close()
    print(s)

part_one()

def part_two():
    f = open('input', 'r')
    found_duplicate = False
    current_freq = 0
    reached_freq = [0]
    while (not found_duplicate):
        for num in f:
            current_freq += int(num)
            if (current_freq in reached_freq):
                print(current_freq)
                found_duplicate = True
                break
            else:
                reached_freq.append(current_freq)
        f.seek(0)
    f.close()
        
part_two()
