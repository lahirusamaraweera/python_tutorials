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

# Hand tracing the algorithm
#   i   j   val..[i]    val..[j]    LIST
#----------------------------------------------
#   0   0   35          35          [35, 11, 54, 10 ]*
#   0   1   35          11          [11, 35, 54, 10 ]
#   0   2   11          54          [11, 35, 54, 10 ]
#   0   3   11          10          [10, 35, 54, 11 ]
#   1   1   35          35          [10, 35, 54, 11 ]*
#   1   2   35          54          [10, 35, 54, 11 ]
#   1   3   35          11          [10, 11, 54, 35 ]
#   2   2   54          54          [10, 11, 54, 35 ]*
#   2   3   54          35          [10, 11, 35, 54 ]
#   3   3   54          54          [10, 11, 35, 54 ]*

value_list = getInputFile()
sorted_list = sortTheList(value_list)
print(value_list)