#reduce
# from functools import reduce
# print(reduce(lambda a,b :a+b,[1,2,3,4,5,6,11]))


# from functools import reduce
# print(reduce(lambda a,b :a if a>b else b,[1,2,3,4,5,6,11]))
# print(reduce(lambda a,b :a if a<b else b,[1,2,3,4,5,6,11]))


#fibnocci
#f(n)=f(n-1)+f(n-2)
num1 ,num2 =0,1
n=10
for i in range(n) :
    print(num1)
    third_num =num1+num2
    num1=num2
    num2=third_num