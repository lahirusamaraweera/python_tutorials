
def isPrimary(n):
    if( n == 1 ): return False
    d = n - 1
    

    while ( d >= 2 ):
        r = n%d
        if r == 0: 
            return False
        d = d - 1

    return True

start  =  int(input("range start : "))
end  =  int(input("range end : "))

if(end > start) : 

    fo = open("primary.txt", "w")
    fo.write('Primary numbers from '+str(start)+' to '+str(end));
    fo.close()

    fo1 = open("primary.txt", "a")
    for i in range (start,end):
        if isPrimary(i):
            print(i)
            fo1.write("\n"+str(i))
    fo1.close()
else :
    print('Invalid number range')