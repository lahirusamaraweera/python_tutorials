from fileio import getInputFile

def searchIfValueExists(search_item, value_list):
    found_count = 0
    for x in value_list:
        if x == str(search_input):
            found_count+=1
    return found_count


# How to search from python
value_list = getInputFile()
search_input = input('Enter a value to search : ')
count = searchIfValueExists(search_input, value_list)
output_string = 'Your search value ' + str( search_input ) + ' found ' + str(count) + ' time(s) in input.txt'
print(output_string)


