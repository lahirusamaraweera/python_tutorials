
x = input('Enter Index number : ')
m1 = input('Enter Index marks for subject 1 :')
m2 = input('Enter Index marks for subject 1 :')
m3 = input('Enter Index marks for subject 1 :')

fo = open("marks.txt", "a")
out = str(x)+" "+str(m1)+" "+str(m2)+" "+str(m3)
fo.write(str(out))
fo.close()