
data_set = open("datasheet.csv")

marks_sheet = [ 
    ['name', 'total', 'average']
]
# loop through line of the document
for data_row in data_set:
    processed_data_row = [];
    index = 0

    total = 0
    #loop through comma separated values of the line
    for data in data_row.strip().split(','):

        #push only the name to the processed data set if the index is zero
        if(0 == index):
            processed_data_row.append(data)
            index+=1
            continue
        int_val = int(data)
        index+=1
        total += int_val
    processed_data_row.append(total)
    processed_data_row.append(total/(index+1))
    marks_sheet.append(processed_data_row)

# output the processed list to the console
print(marks_sheet)

# function to export 2 dimentinal list to a file
def writeListToAFileAsCSV(dataset, fo):
    for line in dataset:
        last = len(line)
        for x in range(0,last):
            tail = ","
            if(x == last-1):
                tail = "\n"
            writetofile(str(line[x])+tail,fo)

def writetofile(text, fo):
    fo.write(text)


fo = open('output.csv', "w")
writeListToAFileAsCSV(marks_sheet, fo)
fo.close()




