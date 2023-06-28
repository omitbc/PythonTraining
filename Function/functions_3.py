def add_fruit(fruit, my_list, price):

    f = fruit
    # print('p {} l {}'.format(id(price), id(my_list)))
    price=200
    print(price)
    # print('p {} l {}'.format(id(price), id(my_list)))
    
    if f not in my_list:
        my_list.append(f)
        print('{} added to list'.format(f))
    else:
        print('{} already in list'.format(f))


list_to_buy = []
price = 100

# print('p {} l {}'.format(id(price), id(list_to_buy)))
add_fruit('orange', list_to_buy, price)
# print('p {} l {}'.format(id(price), id(list_to_buy)))

print(list_to_buy, price)




# -------------------------------------------------------------



price_of_fruits = {
    'orange': 100,
    'watermelon': 200,
    'grapes': 300
}

# shopkeeper started giving discount on every fruit with 10% as default
# discount is a default argument for function
def discount(fruit, discount=0.10):
    # explaing function using docstring
    """
    this function returns price after discount
    """
    discount_rate = discount
    marked_price = price_of_fruits[fruit]

    discount_amount = marked_price * discount_rate
    price = marked_price - discount_amount

    return price

print(discount.__doc__)
print(discount('orange'))
print(discount('orange', 0.60))
print(discount('orange', discount=0.60))