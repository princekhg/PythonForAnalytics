def filetolistofints(file_name):
    list_to_return = []
    with open(file_name) as f:
        line = f.readline()
        while line:
            list_to_return.append(int(line))
            line = f.readline()
    return list_to_return


prime_list = filetolistofints('D:\\EPAM Training\\prime_number.txt')
happie_list = filetolistofints('happynumbers.txt')

overlap_list = [elem for elem in prime_list if elem in happie_list]
print(overlap_list)
