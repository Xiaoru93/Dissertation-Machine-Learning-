#QJF 5.1/5.1.1/5.1.2
list1=[1,2,3]
l=[9,9,9]
x=4
list1.append(x)
print(list1)
list1[len(list1):]=[x]
print(list1)
####
list1.extend(l)
print(list1)
list1[len(list1):]=l
print(list1)
####
list1.remove(2)
print(list1)
####
list1.pop(0)
print(list1)
####
list1.clear()
print(list1)
####
list1=[1,2,3]
l=[9,9,9]
x=4
#-----------
print(list1.index(2))#return the position
##
print(l.count(9))
##
list1.sort(key=None,reverse=True)
print(list1)
##
list1.reverse()
print(list1)
##
lis=list1.copy()
print(lis)
####5.1.1
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # Terry arrives
queue.append("Graham") # Graham arrives
print(queue.popleft()) # The first to arrive now leaves 'Eric'
print(queue.popleft()) # The second to arrive now leaves 'John'
print(queue)# Remaining queue in order of arrival deque(['Michael', 'Terry', 'Graham'])
####5.1.3
squ=[]
for x in range(10):
    squ.append(x**2)
print(squ)
####
squares=list(map(lambda x: x**2, range(10)))
print(squares)
s=[x**2 for x in range(10)]
print(x)
##
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
##
combs=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x !=y:
            combs.append((x,y))
print(combs)
##
vec=[-4,-2,0,2,4]
print([x*2 for x in vec]) # did not change the vec
##
print([x for x in vec if x >= 0],"1") #did not change the vec
print([abs(x) for x in vec])#''
ff=['banana','loganberry','passion fruit']
print([weapon.strip() for weapon in ff])
print([(x, x**2) for x in range(6)])
##
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
##
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
print([[row[i] for row in matrix] for i in range(4)])
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
