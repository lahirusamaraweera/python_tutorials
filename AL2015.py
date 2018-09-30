
# compute
def compute(fo):
    index_no = 0
    while(True):
        index_no = int(input("Enter the index number : "))
        if(-1 == index_no):
            break
        m1 = input('Enter Index marks for subject 1 :')
        m2 = input('Enter Index marks for subject 2 :')
        m3 = input('Enter Index marks for subject 3 :')
        fo.write(compileIndex(index_no, m1, m2, m3))

#complile the required string phase
def compileIndex(index_no, m1, m2, m3):
    return "index_no_"+str(index_no)+", mark_"+str(index_no)+str(m1)+", mark_"+str(index_no)+str(m2)+", mark_"+str(index_no)+str(m3)+"\n"
    

#real execution
#open the file
fo = open("marks.txt", "a")
#call the compute function with the file object
compute(fo)
fo.close()