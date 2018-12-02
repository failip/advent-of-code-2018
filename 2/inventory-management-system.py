def part_one():
    f = open('input', 'r')
    twice = 0
    thrice = 0
    for ID in f:
        ID = ID.rstrip('\r\n')
        letters = list(set(ID))
        for l in letters:
            if (ID.count(l) == 2):
                twice += 1
                break
        for l in letters:
            if (ID.count(l) == 3):
                thrice += 1
                break
    f.close()
    print(f'Twice: {twice}, Thrice: {thrice}, Checksum: {twice*thrice}')

part_one()

def part_two():
    f = open('input', 'r')
    length = len('wlpiogsvdfecjdqmnxakudrhbz')
    found_correct = False
    for ID in f:
        f2 = open('input', 'r')
        for ID2 in f2:
            difference_positions = []
            for i in range(length):   
                if ID[i] != ID2[i]:
                    difference_positions.append(i)
            if len(difference_positions) == 1:
                found_correct = True
                break
        if found_correct:
            print(f'1st ID: {ID[:-1]}')
            print(f'2nd ID: {ID2[:-1]}')
            print(f'Without Difference: {(ID[:difference_positions[0]] + ID[difference_positions[0]+1:])[:-1]}')
            break
        
part_two()