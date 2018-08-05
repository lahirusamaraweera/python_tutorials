def get_inputs(limit):
    list1 = []
    for i in range(0,limit):
        x = input('Enter a number : ')
        list1.append(int(x))
    return list1


def find_max(list1):
    max_val = list1[0]
    list_length = len(list1)
    for i in range(0,list_length):
        if(max_val<list1[i]):
            max_val = list1[i]
    return max_val

def get_sorted_list(list1):
    list_length = len(list1)
    for i in range(0,list_length):
        for k in range(i,list_length):
            if(list1[i]>list1[k]):
                temp = list1[i]
                list1[i] = list1[k]
                list1[k] = temp
    return list1

x = input('how many numbers you have ? :')
#print(find_max(get_inputs(int(x))))
print('Sorted list is : ',get_sorted_list(get_inputs(int(x))))
