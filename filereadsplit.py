fo = open("datafiles/singleline.file",  "r")

line = fo.readline();
values_list = []
sum_values  = 0
for value in line.strip().split(' '):
    int_val = int(value)
    sum_values += int_val
    values_list.append(int_val)

print(values_list)
print(sum_values)