def search(list,key):
    list_count = len(list)
    found_count = 0
    c=0
    while(c<list_count):
        if(key==list[c]):
            found_count=found_count+1
        c=c+1
    return found_count;

list1 = [12,45,41,14,144]



def getIndexIfFound(list1, key):
    list_count = len(list1)
    for i in range(0, list_count):
        if(key == list1[i]):
            return i
    return False;

list_a = ['a', 'b', 'c', 'd', 'e', 'f']
print(getIndexIfFound(list_a,'z'))