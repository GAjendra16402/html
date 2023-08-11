'''def perform_math_operation(a, b, c):
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        result = (a + b) * c
        return result
    else:
        raise ValueError("All three variables must be integers.")
try:
    num1 = 5
    num2 = 67
    num3 = 3
    result = perform_math_operation(num1, num2, num3)
    print(f"The result of ({num1} + {num2}) * {num3} is: {result}")
except ValueError as e:
    print(e)'''
#-----------------for loop
'''for i in range(5,100,6):
  print(i)'''
  
'''a='mohit'
count = 0
for i in range(0,len(a)):
 if(a[i]=='a' or a[i]=='e' or a[i]=='o' or a[i]=='i' or a[i]=='u'):  
     count = count + 1 
print(count)'''


'''number = 89576
num_str = str(number)
result = 0

for i in range(len(num_str)):
    if i == 0 or i == len(num_str) - 1:
        result += int(num_str[i])

print(result)'''

'''import string

user_password = input("Enter a password: ")

if len(user_password) < 8 or not user_password[0].isupper():
    print("Password is unsafe.")
else:
    has_number = False
    has_special = False

    for char in user_password:
        if char.isdigit():
            has_number = True
        if char in string.punctuation:
            has_special = True

    if has_number and has_special:
        print("Password is safe.")
    else:
        print("Password is unsafe.")'''

#--------------------------------------------------------------------
'''for i in range (0,5):
    for j in range(0,5):
        print(j,end="")
    
    print("\n")
    
    
#------------------------------------------------------------------------
for i in range(0,5):
    print("*" * i)



    
#-------------------------------------------------------------------------
for i in range(1, 5):
    print('*' * i)

#---------------------------------------------------------------------
for i in range(1, 5):
    for j in range(i):
     print(i,end="")
     
    print("\n")
    
#------------------------------------------------------------------
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("\n")
    
#--------------------------------------------------------------------
for i in range(0,5):
    for j in range(0,5):
        if(j==0 or j==4):
         print(i,end="")
        else:
            print(end=" ")
    print("\n")'''