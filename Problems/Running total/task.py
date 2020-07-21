number = [int(x) for x in str(int(input()))]
sequence = [sum(number)]
for index, num in enumerate(reversed(number), 0):
    sequence.append(sequence[index] - num)

sequence.reverse()
sequence.remove(0)
print(sequence)
