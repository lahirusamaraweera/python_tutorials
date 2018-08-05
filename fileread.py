def binarysearch(list, item):
    first =0
    last=len(list)-1
    found=False

    while first<=last and not found:
        midpoint=(first+last)//2
        if list[midpoint]==item:
            found = True;
        else:
            if item<list[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
        return found 


fo = open("data2.txt", "r")
string = fo.readlines()
list1 = []
for x in string :
    list1.append(int(x))
print(list1)
print(binarysearch(list1, 12))






