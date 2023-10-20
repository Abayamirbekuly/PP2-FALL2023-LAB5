def game(nums):
    
    found_0, found_0_2, found_7 = False, False, False

    for num in nums:
        if not found_0 and num == 0:
            found_0 = True
        elif found_0 and not found_0_2 and num == 0:
            found_0_2 = True
        elif found_0 and found_0_2 and num == 7:
            found_7 = True
            break

    return found_0 and found_0_2 and found_7


user_input = input("Enter: ")
user_numbers = [int(x) for x in user_input.split()]

result = game(user_numbers)
if result:
    print("true.")
else:
    print("false.")
