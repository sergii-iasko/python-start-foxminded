products: dict = {
    'iphone': ['phone', 'electronics'],
    'bmw': ['cars', 'metal'],
    'flower': ['alive'],
    'egg': ['food', 'cheap']
}


def print_tags(tags: list):
    for tag in tags:
        print(tag)


while products:
    prod = input('Enter the product name: ')

    if prod in products:
        print_tags(products[prod])
        del products[prod]
    else:
        print('There is no such product:(')

print('We ran out of products!')
