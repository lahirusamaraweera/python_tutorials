
# functions
def addnumbers(a, b):
    return a + b


# result = addnumbers(3,5) #invoking the addnumbers function / calling the addnumbers function
# print(result)

def isEven(a):
    r = a % 2
    if( 1 == r ):
        return False
    return True


result = isEven(4)
print(result)
result1 = isEven(5)
print(result1)
