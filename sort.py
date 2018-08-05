def sortthis(list1):
    for i in range(len(list1)-1):
            for k in range(i,len(list1)):
                if list1[i]>list1[k]:
                    abc = list1[i]
                    list1[i],list1[k]=list1[k],abc
    return list1


list_sample  =  [ 26, 25, 14, 55, 1, 2, 5 ]
print(sortthis(list_sample))