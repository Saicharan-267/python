#odd or even

# def even_or_odd(num1):
#     if num1%2==0:
#         print("even")
#     else:
#         print("odd")
# even_or_odd(8)       

#vote 

# def person_eligible(age):
#     res="vote" if age>=18 else 'not eligible'
#     print(res)
# person_eligible(19)    

#greatest of 2 numbers

# def check_greatest (num1,num2):
#     return num1 if num1> num2 else num2
# print(check_greatest(4,5))

# #2
# def check_greatest (num1,num2):
#     if num1>num2:
#        return num1
#     elif num1==num2:
#         return 'both are equal'
#     else :
#         return num2
# print(check_greatest(4,5))   


#simple calculator to perform add,sub,mult,div

def simple_cal(n1,n2,op):
    if op=='+'or 'add':
        print(n1+n2)
    elif op=='-'or 'sub':
        print(n1-n2) 
    elif op=='*' or'mul':
        print(n1*n2)  
    elif op=='/'or 'div' :
        print(n1/n2) if n2!=0 else print('not possible')
num1=int(input('enter 1st number'))
num2=int(input('enter 2nd number'))
input_op=input ('enter opration')

simple_cal(num1,num2,input_op)



