# Print numbers from 1 to 20
# for i in range(1,21):
#     print(i)
# for i in range(2, 51,2):
#     print(i)
# for i in range(1,51):
#     if i%2==0:
#         print(i,"Even")








# Multiplication table
# n=int(input("enter the number"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)







# Reverse a number
# n=int(input("enter the number"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print("Reverse number",rev)



# Simple Calculator
a=int(input("enter the number:"))
b=int(input("enter the value:"))
print("1.add,2.sub,3.mul,4.div")
choice=int(input("enter the choice:"))
if choice ==1:
    print(a+b)
elif choice ==2:
    print(a-b)
elif choice ==3:
    print(a*b)
elif choice ==4:
    print(a/b)
else:
    print("Invailld choice")