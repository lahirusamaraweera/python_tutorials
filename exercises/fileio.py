def appendToTheOutputFile(content):
    output_file_object = open('output.txt', 'a+')
    output_file_object.write(content)
    output_file_object.write('\n')
    output_file_object.close()

def clearFile():
    output_file_object_1 = open('output.txt', 'w')
    output_file_object_1.write('')
    output_file_object_1.close()

def add1(x):
    return x + 1


def getInputFile():
    file_object = open('input.txt','r') # opening the file with read permissions
    read_content = file_object.read()
    return read_content.split(',')


