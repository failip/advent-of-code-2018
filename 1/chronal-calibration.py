f = open('input', 'r')
s = 0
for num in f:
    s += int(num)
print(s)

f.seek(0)
found_duplicate = False
current_freq = 0
reached_freq = {}
while (not found_duplicate):
    for num in f:
        current_freq += int(num)
        if (current_freq in reached_freq):
            print(current_freq)
            found_duplicate = True
            break
        else:
            reached_freq[current_freq] = 0
    f.seek(0)
f.close()
