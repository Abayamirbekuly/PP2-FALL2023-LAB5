
       
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]


prime_numbers = list(filter(lambda x: is_prime(x), numbers))


print("Prime numbers in the list:", prime_numbers)
