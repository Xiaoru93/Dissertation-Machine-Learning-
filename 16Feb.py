#WXP 5.2
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
##
del a[2:4]
print(a)
del a[:]
print(a)
del a
# print(a)
###
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
###
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b)# letters in a but not in b
print(a|b)# letters in either a or b
print(a&b)# letters in both a and b
print(a^b)# letters in a or b but not both
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
####ZWJ5.5
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x ** 2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))

