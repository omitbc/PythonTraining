# list_to_buy list should always be available
list_to_buy = []

def add_fruit(fruit):

    f = fruit

    if f not in list_to_buy:
        list_to_buy.append(f)
        print('{} added to list'.format(f))
    else:
        print('{} already in list'.format(f))


def remove_fruit(fruit):

    f = fruit
    
    if f in list_to_buy:
        list_to_buy.remove(f)
        print('{} removed from list'.format(f))
    else:
        print('{} not in list'.format(f))

# first class function
fruit = add_fruit
fruit('orange')

add_fruit('orange')
add_fruit('watermelon')
add_fruit('grapes')
remove_fruit('orange')
fruit('watermelon')

print(list_to_buy)



# --------------------------------------------------------------------------------


# packing
def add_to_list(*args):
    if args is not None:
        for f in args:
            print(f)

add_to_list('apple', 'papaya')


# unpacking
def add_to_bag(fruit_1, fruit_2, fruit_3):
    print(fruit_1, fruit_2, fruit_3)

fruits = ['orange', 'watermelon', 'apple']
add_to_bag(*fruits)


# packing
def add_to_basket(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

add_to_basket(orange=100, watermelon=200, grapes=300)


# unpacking
def add_to_jhola(orange, watermelon, grapes):
    print('{} {} {}'.format(
        orange,
        watermelon,
        grapes))

price_of_fruits = {
    'orange': 100,
    'watermelon': 200,
    'grapes': 300
}

add_to_jhola(**price_of_fruits)