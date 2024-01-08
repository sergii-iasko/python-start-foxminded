products: dict = {
    'iphone': ['phone', 'electronics'],
    'bmw': ['cars', 'metal'],
    'flower': ['alive'],
    'egg': ['food', 'cheap']
}

while products:
    prod = input('Enter the product name: ')
    if prod in products:
        for tag in products[prod]:
            print(tag)
        del products[prod]
    else:
        print('There is no such product:(')

print('We ran out of products!')