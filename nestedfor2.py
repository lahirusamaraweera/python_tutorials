

for i in range(0, 11):
    st = ''
    for x in range(0,11):
        if(x != i):
            st = st + ' * '
        else:
            st = st + ' + '
    print(st)



