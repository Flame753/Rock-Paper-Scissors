height = int(input())
space = ' '
hash = '#'
for x in range(1, height+1):
    print(space*(height-x) + hash*(x*2-1))
