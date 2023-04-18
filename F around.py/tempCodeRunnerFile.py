def max_num_in_list(a_list):
    max = a_list [0]
    for num in a_list:
        if num > max:
            max = num
    return max

print(max_num_in_list([45,-9,8675,3,66]))