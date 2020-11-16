if index < 0:
    index = index * -1
    while i < index + 1:
        indexed_list.append(number_list2[i])
        i += 1
    for numbers in number_list1:
        indexed_list.append(numbers)
    while i < len(number_list2):
        indexed_list.append(number_list2[i])
        i += 1
    return indexed_list

   # I originally thought that the second list had to be spliced into the first if the index was negative, this is solving that