
list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist1 = [123, 'john']

list1[0] = 'test'

print list1          # Prints complete list1
print list1[0]       # Prints first element of the list1
print list1[1:3]     # Prints elements starting from 2nd till 3rd 
print list1[2:]      # Prints elements starting from 3rd element
print tinylist1 * 2  # Prints list1 two times
print list1 + tinylist1 # Prints concatenated list1s