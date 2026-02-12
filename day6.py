# def add(a,b):
#     return a+b
# print(add(10,20))
# Function to check even or odd
# def even_odd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(10))





# Factorial function
# def facta(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# print(facta(5))
 






# ✅ Reverse Number Function
# def reva(n):
#     rev=0
#     while n>0:
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     return rev
# print(reva(123))

# n=int(input("enter the number:"))
# if n%2==0:
#         print("even")
# else:
#         print ("odd")

# a=int(input("enter the number  frist :"))

# b=int(input("enter the number second :"))

# c=int(input("enter the number thrid :"))
# if a>b and a>c:
#     print("a")
# elif b>a and b>c:
#     print("b")
# else:
#     print("c")
# n=int(input("enter the number :"))
# for i in range(0,11):
#     print(n,"*",i,"=",n*i)
# n=input("enter the name ")
# print(n[::-1])

# def facter(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# num=int(input("enter the number :"))
# print( facter(num))

# def is_palindrome(s):
#     s.lower()
#     return s ==s[::-1]
# text=input("enter name :")
# if is_palindrome(text):
#     print("palindrome")
# else:
#      print(" not palindrome")




# 22️⃣ Write a function to count vowels in a string
# def cout(n):
#     v='aeiouAEIOU'
#     count=0
#     for ch in n:
#         if ch in v:
#             count+=1
#     return count
# text=input("enter name")
# print(cout(text))
# n=[10,20,30,40,50]
# l=n[0]
# t=0
# for num in n:
#     t+=num
#     if num>l:
#         l=num
# print(t)
# print(l)
# n=list(input("enter the values"))
# print(n[::-1])

num=[0,1,2,0,3,0,4,0,0]
r=[]
for numbers in num:
    if numbers!=0:
        r.append(numbers)
print(r)
