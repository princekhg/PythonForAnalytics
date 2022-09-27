def max_three(num_1, num_2, num_3):
    if num_1 > num_2:
        if num_1 > num_3:
            return num_1
        else:
            return num_3
    elif num_2 > num_1:
        if num_2 > num_3:
            return num_2
        else:
            return num_3
    elif num_3 > num_1:
        if num_3 > num_2:
            return num_3
        else:
            return num_2


print(max_three(10, 90, 45))