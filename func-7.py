def ha(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


inputl = input("integers : ")
user_numbers = [int(x) for x in inputl.split()]

result = ha(user_numbers)
if result:
    print("true")
else:
    print("false")
