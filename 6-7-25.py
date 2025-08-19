# n1,n2,n3=2,3,4
# if n1>n2 and n1>n3:
#     print(n1)
# elif  n2>n1 and n2>n3:
#     print(n2)
# else:
#     print(n3)


#leap year

def check_leap(year):
    if year<0:
        return('Invalid year')
    if year % 400 ==0:
        return('leap year')
    elif (year % 100!=0 and year % 4==0):
        return('leap year')
    else:
        return( 'not a leap year')
input_year=int(input('enter a year'))
res=check_leap(input_year)
print(res)

# vowel ,consonant,neither

# input_char=input('enter char').upper()
# def check_vowel_consonant_other(char):
#     if len(char)!=1:
#         return 'invalid '
#     if char in 'AEIOU':
#      print ('vowels')
#     else:
#       print('consonant')
# check_vowel_consonant_other(input_char)
