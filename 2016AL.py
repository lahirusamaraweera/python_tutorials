def getprice(i):
    price_list = [ 10.00, 12.00, 15.00]
    return price_list[i-1]


while(True):
    no_of_food_items = int(input('How many food items are there ? '))

    total_price = 0.0
    for i in range(0, no_of_food_items ):
        item_id = int(input('Enter the item id '))
        number_of_items = int(input('Enter the qty '))
        total_price += (number_of_items * getprice(item_id))

    print('total = '+str(total_price))