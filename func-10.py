def uniquel(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


uinput = input("Enter : ")
user_list = uinput.split()

unique_list = uniquel(user_list)
print("unique elements:", unique_list)
