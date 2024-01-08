a: list = [4, 6, 45, 'Hello', 'world']

a.append(55)
print(a)

a.pop(5)
print(a)

obj = a.pop()
print(obj)

c = a[:2]
print(c)

s = "hello"
print(list(s))

d = [4, 5]
g = [6, 7]
result = d + g
print(result)