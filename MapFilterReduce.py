# MAPS
def cube(x):
    return x*x*x

l=[1,2,3,4,5]
# newl = []
# for i in l:
#     newl.append(cube(i))
newlist=list(map(cube,l))
print(newlist)
 
# Filter
def filter_function(a):
   return a>4
newl = list(filter(filter_function,l))
print(newl)

# Reduce Function
from functools import reduce
def mysum(x,y):
    return x+y
sum = reduce(mysum,l)
print(sum)