a: set = {4, 5, 6, 'hello'}
b: set = {4, 5, 8, 'world'}
# set is unordered item. we can't use indes like a[0]
# set contains only unique objects
result_1 = a.intersection(b)
result_2 = a.union(b)

s = a & b #intersection
s = a | b #union


print(result_1)
print(result_2)

a.discard('hello')