# fo = open("data.txt", "r")
# string = fo.readlines()
# print(string)

# fo.close()

def printwithLB(text, fo):
    fo.write(text+"\n")

fo = open("final.csv", "")
for x in ['name', 'game','same']:
    printwithLB(x,fo)
fo.close()



# fo = open("data2.txt", "a")
# fo.write( "Buwaneka.\nWishwanawath\n")
# fo.close()  

