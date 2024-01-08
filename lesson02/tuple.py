# tuple can't be changed, while lists can
k: tuple = (5, 6, 'hello')
s: tuple = (7, 8)
result = k + s
print(result)