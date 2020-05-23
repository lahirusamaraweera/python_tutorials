# write a program to generate the binary value sting for a given decimal number
# and also print whether the number is odd or even

# 10  => '1010'
# 5 => '101'

input_number = input("enter the number : ")

binary_value_string = ''
a = input_number # eg : [0,1,0]
rem_list = []
number_type = ''


odd_even_rem = a % 2
if odd_even_rem == 1:
    number_type = 'Odd number'
else:
    number_type = 'Even number'


while a > 0:
    r = a % 2
    rem_list.insert(0, r)
    binary_value_string = str(r) + binary_value_string 
    a = a // 2

# hand trace table for the above iteration
# a   r   bi_tring    rem_list
# 10  0   '0'         [0]
# 5   1   '10'        [1,0]    
# 2   0   '010'       [0,1,0],
# 1   1   '1010'      [1,0,1,0]

print(rem_list)
print(binary_value_string)
print(number_type)