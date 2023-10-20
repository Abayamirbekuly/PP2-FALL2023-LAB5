def histogram(numbers):
    for num in numbers:
        print('*' * num)


uinput = input("Enter: ")
user_numbers = [int(x) for x in uinput.split()]

histogram(user_numbers)
