# num1=12534
# print(len(str(num1)))
# str1=str(num1)
# sum=0
# for i in str1:
#     sum=sum+int(i)
# print(sum)
# print(int(str(num1)[::-1]))

# num1=2456
# count=0
# sum=0

# while num1>0:
#     rem=num1%10
#     print(rem)
#     # que=num1//10
#     # num1=que
#     num1=num1//10

# while num1>0:
#     rem=num1%10
#     print(rem)
#     num1=num1//10
#     count+=1
#     sum+=rem

# print(count)
# print(sum)

def count_freed_prisoners(prison_cells):
    freed_count = 0
    state = 1  # 1 means current expectation: unlocked, 0 means locked

    for cell in prison_cells:
        if cell == state:
            freed_count += 1
            state = 1 - state  # flip the expected state
    return freed_count

# Read input from STDIN
prison_cells = map(int, input().strip().split())

# Call the function and print the result
print(count_freed_prisoners(prison_cells))