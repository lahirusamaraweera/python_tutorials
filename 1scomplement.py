
def getBinary(n):
    if n == 0 :
        return '0'
    is_negative = False

    bin_str = ' '
    if( n < 0 ) :
        is_negative = True  
        n *= (-1)

    d = n
    while(d > 0):
        r = d%2
        if(is_negative):
            if(r==1):
                bin_str = str(0)+bin_str
            else:
                bin_str = str(1)+bin_str
        else :
            bin_str = str(r)+bin_str
        d//=2

    return bin_str


while True:
    n = int(input("Enter the Decimal number : "))
    print('1\'s complement value of '+str(n)+' is '+str(getBinary(n)))
