import math
import os


def getSquareRoot(val):
    return math.sqrt(val)


def createDir(name):
    os.mkdir(name)
    

def deleteDir(name):
    os.rmdir(name)


#result  = getSquareRoot(25)
#print(result)

createDir('KEeth')