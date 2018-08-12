def sortUsingFor(list1, is_acending = True):
    for i in range(len(list1)):
            for k in range(i+1,len(list1)):
                if(is_acending):
                    if list1[i]>list1[k]:
                        temp = list1[i]
                        list1[i],list1[k]=list1[k],temp
                else:
                    if list1[i]<list1[k]:
                        temp = list1[i]
                        list1[i],list1[k]=list1[k],temp
    return list1

    
def sortUsingWhile(list1):
    i = 0
    while(i < len(list1)):
        k = i+1
        while(k < len(list1)):
            if list1[i]>list1[k]:
                    temp = list1[i]
                    list1[i],list1[k]=list1[k],temp
            k +=1
        i += 1
    return list1

list_sample  =  [ 26, 25, 14, 55, 1, 2, 5 ]
print(sortUsingFor(list_sample, False)) 
print(sortUsingWhile(list_sample))