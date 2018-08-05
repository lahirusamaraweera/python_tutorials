
def sorting(list1,type):
    if type == "ASC":
        for i in range(len(list1)-1):
            for k in range(i,len(list1)):
                if list1[i]>list1[k]:
                    abc = list1[i]
                    list1[i],list1[k]=list1[k],abc
    if type == "DSC":
        for i in range(len(list1)-1):
            for k in range(i,len(list1)):
                if list1[i]<list1[k]:
                    abc = list1[i]
                    list1[i],list1[k]=list1[k],abc
    return list1

#www = sorting(list1,"ASC")
#print(list2)
kkk = sorting(x,"DSC")
#print(www)
print(kkk)
