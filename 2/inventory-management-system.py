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
    print(f'Twice: {twice}, Thrice: {thrice}, Checksum: {twice*thrice}')

part_one()

