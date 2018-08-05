fo = open("data.txt", "r")
string = fo.readlines()
print(string)

fo.close()

fo = open("data2.txt", "w")
fo.write( "Buwaneka.\nWishwanawath\n")
fo.close()

fo = open("data2.txt", "a")
fo.write( "Buwaneka.\nWishwanawath\n")
fo.close()  

