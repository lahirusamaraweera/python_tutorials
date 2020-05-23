

tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple1 = (123, 'john')

# tuple1[0] = 'test' # tuple object doesn's support item assignment

print tuple1           # Prints complete list
print tuple1[0]        # Prints first element of the list
print tuple1[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple1[2:]       # Prints elements starting from 3rd element
print tinytuple1 * 2   # Prints list two times
print tuple1 + tinytuple1 # Prints concatenated lists