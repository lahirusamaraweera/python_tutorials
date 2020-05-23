from fileio import getInputFile, appendToTheOutputFile, clearFile

clearFile()
value_list = getInputFile()

print(value_list)
value_list = map(int, value_list)
print(value_list)

sum_1 = sum(value_list)
appendToTheOutputFile('sum = ' + str(sum_1) )