
vallist = [45,200,45,780,44,450]
val_length = len(vallist)

max_val = vallist[0]

for i in range (0,val_length):
    
    if(max_val<vallist[i]):
        max_val = vallist[i]

print(max_val)