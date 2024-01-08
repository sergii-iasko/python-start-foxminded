# f = open('text.txt', 'r')
# text = f.read()
# print(text)
#
# f.close()

#============================

# f = open('text.txt', 'rb')
# text = f.read()
# print(text)
#
# f.close()

#============================

# f = open('text.txt', 'w')
# f.write('hello dear')
# f.close()

#============================
#
# f = open('text.txt', 'a')
# f.write('\nHello World\n')
# f.close()

#============================

with open('text.txt', 'r') as f:
    # print(f.read())
    print(f.readlines())

