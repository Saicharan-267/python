#15 ,30,45,60,75 ,comon multiples of 3 ,5
print(list(range(15,400,15)))

#set--unordred ,finite,unique elements
#set only take immutable elements but set itself is mutable
set1={4,5,'str1',9.5,(1,2,3)}
print(set1)

list1=[1,1,1,22,3,3,"str1",'str1']
#
# print(set(list1))
print(list(set(list1)))

set1={1,2,3,{4,5,6}}
print(set1)

fset1=frozenset([1,2,3,4,3,])
print(fset1)

