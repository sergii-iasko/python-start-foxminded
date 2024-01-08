a = 5
b = 7
c = 8

# if a == b:
#     print("a and b equal")
# else:
#     print('a and b are not equal')

if b < c and a == b:
    print('first')
elif b < c:
    print('second')
else:
    print('final')

print(not bool(a))

s = {5, 6, 7}

if a in s:
    print('inside')