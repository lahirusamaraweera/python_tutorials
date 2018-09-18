
kesel_kana = open("kanishka.ridmika")
# values = fo.readlines()
# print(values)


kesel_bajanaya = []
sum_values = 0
for kesel_avary in kesel_kana:
    anu_kesel_bajanaya = []
    for kesel_gedi in kesel_avary.strip().split(' '):
        int_val = int(kesel_gedi)
        sum_values += int_val
        anu_kesel_bajanaya.append(int_val)
    kesel_bajanaya.append(anu_kesel_bajanaya)
print(kesel_bajanaya)
print(sum_values)