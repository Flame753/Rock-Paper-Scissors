numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file = open('file_with_list.txt', 'w')
print(numbers, file=file, flush=True, end='')
file.close()
