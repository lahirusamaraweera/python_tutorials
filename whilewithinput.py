print('Please provide the range')
min_val = int(input("enter the min : "))
max_val = int(input("enter the max : "))

if(min_val > max_val ):
    print('min should be less than max')
else:
    value_list = []
    c = min_val
    while(c < max_val ):
        value_list.append(c)
        c+=1
    print(value_list)