# put your python code here
first_number = float(input())
second_number = float(input())
operation = str(input())


def div_by_zero(num):
    if num == 0:
        print('Division by 0!')
        return True
    return False


if operation == '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
elif operation == '/' and not div_by_zero(second_number):
    print(first_number / second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == 'mod' and not div_by_zero(second_number):
    print(first_number % second_number)
elif operation == 'pow':
    print(first_number ** second_number)
elif operation == 'div' and not div_by_zero(second_number):
    print(first_number // second_number)
