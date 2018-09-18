# read file and transform data into a python list=> [ [], [] ]
def readAndCacheData(file_name):
    data_set = open(file_name+".csv")
    marks_sheet = []
    # loop through line of the document
    for data_row in data_set:
        processed_data_row = []
        for data in data_row.strip().split(','):
            processed_data_row.append(data)

        marks_sheet.append(processed_data_row)
    return marks_sheet

# search the given marks_sheet with given keyword
def searchResult(keyword, marks_sheet):
    for result in marks_sheet:
        if(result[0] == keyword):
            printResult(result)

# print the given result
def printResult(result):
    print('Name : '+str(result[0]))
    print('Total : '+str(result[1]))
    print('Average : '+str(result[2]))
    print('---------------------------')

#initialization
file_name = raw_input('enter the name of the file : ')
marks_sheet = readAndCacheData(file_name)
while(True):
    keyword = raw_input("Name of the student : ")
    searchResult(keyword,marks_sheet)
            


