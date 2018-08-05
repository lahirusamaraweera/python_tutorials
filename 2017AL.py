def ask_for_value(show_additional_word = '', as_a_int = True):
    show_this = 'Please enter a value for '
    user_input = raw_input(show_this+show_additional_word+' : ')
    if(as_a_int):
        return int(user_input)
    else:
        return user_input

def get_unit_prices():
    return {
        '64<' : 5,
        '64>' : 10
    }

def calculate_monthly_bill():
    house_number = ask_for_value('house number', False)
    pm_reading = ask_for_value('Past month reading')
    cm_reading = ask_for_value('Current month reading')

    price_list = get_unit_prices()

    number_of_units = cm_reading - pm_reading
    price = 0
    if(number_of_units > 64 ):
        price = (64*price_list['64<']) + ( ( number_of_units-64 ) * price_list['64>'] )
    else:
        price = number_of_units*price_list['64<']
    
    return { 'house number': house_number, 'price' : price }


while(True):
    print(calculate_monthly_bill());