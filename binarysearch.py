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

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,56]
print(binarysearch(testlist, 3))
print(binarysearch(testlist, 13))
