
def count_items(given_list):
    i = 0
    for item in given_list:
        i =i+1
    
    return i



#sample_list = [254,154,254542]
#print count_items(sample_list)

#sample_list = [254,154,454, 45545,54654]
#print count_items(sample_list)

#sample_list = [5454, 545,545,454]
#print c

def ask_for_value(show_additional_word = ''):
    show_this = 'Please enter a number for '
    return int(input(show_this+show_additional_word+' : '))


def get_input_form_usr():
    range_min = ask_for_value('min')
    range_max = ask_for_value('max')
    
    li = []
    if(range_min > range_max ):
        return li

    for i in range(range_min, range_max+1):
        li.append(i)
    return li


sample_list = get_input_form_usr()
print(sample_list)
