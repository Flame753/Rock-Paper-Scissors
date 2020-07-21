# read sums.txt
file = open('sums.txt', 'r')
for line in file:
    list_line = line.split()
    print(int(list_line[0]) + int(list_line[1]))
file.close()
