#jump statements 
#break

# for i in range(1,20):
    
#     if i==5:
#         break
#     print(i)


# for i in range(1,20):
#     print(i)
    
#     if i==5:
#         break
    
# for i in range (1,30):
#     if i<i*(-1):
#          break
#     print(i)

#continue

# for i in range(1,10):
#     print(i)
#     print(i)
#     if i==6:
#         continue 
#     print(i)

# for class_no in range(1,11):
#     if class_no==4:
#         break
#     for roll_no in range (1,31):
#         if roll_no==5:

        
#             print ('class',class_no,'roll',roll_no)


# for class_no in range(1,11):
#     if class_no==4:
#         break
#     for roll_no in range (1,10):
#         if roll_no==5:
#             continue
#         print ('class',class_no,'roll',roll_no)

#pass

# num1=11
# if num1 %2==0:
#     pass
# else:
#     print('number is odd')

for class_no in range(1,11):
    for roll_no in range (1,10):
        if class_no%5==0 or roll_no<15:
            break
        print ('class',class_no,'roll',roll_no)

