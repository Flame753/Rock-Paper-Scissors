# put your python code here
first_number = float(input())
second_number = float(input())
operation = str(input())


def division_by_zero(num):
    if num == 0:
        print('Division by 0!')
        return True
    return False


if operation == '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
elif operation == '/':
    if not division_by_zero(second_number):
        print(first_number / second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == 'mod':
    if not division_by_zero(second_number):
        print(first_number % second_number)
elif operation == 'pow':
    print(first_number ** second_number)
elif operation == 'div':
    if not division_by_zero(second_number):
        print(first_number // second_number)
