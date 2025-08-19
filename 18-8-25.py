#lambda function---anonymous one line function in python 

exam_fun= lambda a,b:a+b
print(exam_fun(4,6))

lam1=lambda a:a**2
print(lam1(10))

#why lambda function
#Geneerally there are used in higher order function
#map, filter and reduce
#map (function ,iterable)

def square(x):
    return x**2
print(list(map(square,[1,2,3,4,5,6])) )

#filter
#filter (function,iterable)

print(tuple(filter(lambda x:x%2 ==0,[1,88,71,32,44,57,91])))
