# #function scope

# num1=10
# def check_function():
#     num2=20
#     print(num1)
#     print(num2)

# check_function() 

# #global scope
# #we can use anywhere after decleartion

# num1=10
# def check_function()
#     num2=20
#     print(num1)
#     print(num2)
# check_function()

# #local function
# #we can use inside function only
# def check_function()
#     num2=20
#     print(num2)
# check_function()

# #enclosed scope

# def outer_function():
#     str1='mrngg'
#     def inner_function():
#         print(str1)
#     inner_function()
# outer_function()

#built in --- for some builtin 


# num1=10
# def check_scope():
#     num1=20
#     print(num1)
# # check_scope()
# # print(num1)

# user_name='charan' 
# def first_function():
#     user_name='varun'
#     def second_function():
#         user_name='teja'
#         print(user_name)
#     second_function()
#     print(user_name)
# first_function()
# print(user_name)

# num1=10
# def check_function():
#     global num1
#     num1=20
#     print(num1)
# check_function()
# print(num1)

num1=10
def check_function():
    num1=20
    globals()['num1']=30
    print(num1)
check_function()
print(num1)
        