

val = 90

if val<35:
    print('F')
elif val<45:
    print('S')
elif val<75:
    print('B')
else:
    print('A')


a,b = 4,5
print(a)
print(b)

a,b = b,a
print(a)
print(b)

a =b =5
print(a)
print(b)

d = 3-4*6/3+12/4*3
print(d)

def calc(x, y=6):
    return x*y

print(calc(9,4))