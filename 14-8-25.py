num1=25
def first_function():
    num1=35
    def second_function():
        nonlocal num1
        num1=45
        print(num1)
    second_function()
    print(num1)
first_function()  
print(num1)

#prime number

count=0
for i in range(1,num1+1):
    if num1%i==0:
        