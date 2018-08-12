
def getInputList(display = 'Enter a number : '):
    val = 0
    value_list = []
    while(val != -1):
        val = int(input(display))
        if(val != -1):
            value_list.append(val)

    return value_list


def askTheCondition(display = 'Do you want to sort ASC or DSC (ASC=1) / (DSC=anything) : '):
    condition = int(input(display))
    if(1 == condition ):
        return True
    else:
        return False

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
 

sorted_list = sortUsingFor(getInputList(),askTheCondition())





