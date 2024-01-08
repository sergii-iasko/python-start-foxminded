products: dict = {
    'iphone': ['phone', 'electronics'],
    'bmw': ['cars', 'metal'],
    'flower': ['alive'],
    'egg': ['food', 'cheap']
}


def print_tags(tags: list):
    file_name = 'tags.txt'
    with open(file_name, 'a') as f:
        for tag in tags:
            f.write(tag + '\n')

    print('Products found. The tags are in file %s' % file_name)


while products:
    prod = input('Enter the product name: ')

    if prod in products:
        print_tags(products[prod])
        del products[prod]
    else:
        print('There is no such product:(')

print('We ran out of products!')
