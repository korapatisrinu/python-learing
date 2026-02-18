

# 👉 Write program to count digits in a number

# Example:

# Input: 54879
# Output: 5

# (Hint: use while loop)

# n=54678

# c=0
# while n!=0:
#     n=n//10
#     c+=1
# print(c)






# n=int(input("enter the number:"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")



# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)




# n=int(input("entr number"))
# c=0
# while n!=0:
#     n=n//10
#     c+=1
# print(c)


# ❓ Q1 — Create Class Student

# Requirements:

# ✔ name
# ✔ marks
# ✔ method to display details

# 👉 Write Python code.


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def dispay(self):
#         print("Name:",self.name)
#         print("marks:",self.marks)
# s1=Student("nani",90)
# s1.dispay()

# ✏️ 1) Palindrome Program

# # 👉 Check number is palindrome or not
# num=int(input("enter the number:"))
# o=num
# rev=0
# if num<0:
#     print(" Not palindrome")

# while num>0:
#     d=num%10
#     rev=rev*10+d
#     num=num//10
# if o==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

# text="madam"
# if text==text[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")






# 1) Fibonacci Series
n=int(input("enter the number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

# Prime Number Check
n=int(input("enter the number"))
if n <=1:
    print("not a prime number")
else:
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    if is_prime:
        print("prime")
    else:
        print("not prime")
# 3) Reverse String (without shortcut)
n=input("enter the string:")
rev=""
i=len(n)-1
while i>=0:
    rev+=n[i]
    i-=1
print(rev)