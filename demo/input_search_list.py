def getInputList(display = 'Enter a number : '):
    val = 0
    value_list = []
    while(val != -1):
        val = int(input(display))
        if(val != -1):
            value_list.append(val)

    return value_list


def indexOfList(list_, key):
    found_indices = []
    for i in range(len(list_)):
        if(key == list_[i]):
            found_indices.append(i)
    
    return found_indices


value_list = getInputList();
index = indexOfList(value_list, 90);
print(value_list)
print(index)