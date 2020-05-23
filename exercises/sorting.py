from fileio import getInputFile

def sortTheList(value_list):
    value_list = map(int, value_list)
    for i in range(len(value_list)):
        for j in range(i, len(value_list)):
            if value_list[i] > value_list[j]:
                temp = value_list[i]
                value_list[i] = value_list[j]
                value_list[j] = temp
    
    return value_list

value_list = getInputFile()
sorted_list = sortTheList(value_list)
print(value_list)