# Q1


# x = [1, 2, 3]
# y = x
# y.append(4)
# print(x)

# Q2
# print("AI Engineer"[::-2])
#    codeing 



# Q7 — Remove Vowels

# Input:

# "python engineer"


# Output:

# "pythn ngnr"


# text="python engineer"
# v="aeiouAEIOU"
# r=""
# for ch in text:
#     if ch not in v:
#         r+=ch
# print(r)



# 🔵 Next Question
# Q8 — Move Zeros to End

# Input:

# [0,1,0,3,12]


# Output:

# [1,3,12,0,0]

# num=list(map(int,input("enter the  nu ber :").split()))
# r=[]
# for i in num:
#     if i!=0:
#         r.append(i)
# zero_count=num.count(0)
# for num in range(zero_count):
#     r.append(0)
# print(r)





# Q9 — File Handling

# Write program to:

# 1️⃣ Save 3 names to a file
# 2️⃣ Read and print them

# with open("names.txt","w") as f:
#     f.write("nani\n")
#     f.write("Srinivas\n")
#     f.write("Ram\n")
# with open("names.txt","r")as f:
#     data=f.read()
#     print(data)
   








# Create class Laptop:

# Attributes:

# brand

# price

# Methods:

# apply_discount(percent)

# display()


# class Laptop:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def apply_discount(self,percent):
#         discount=self.price*percent/100
#         self.price-=discount
#     def display(self):
#         print("Brand:",self.brand)
#         print("Price",self.price)
# l1=Laptop("Dell",80000)
# l1.apply_discount(10)
# l1.display()





# n=1234
# r=0
# while n>0:
#     d=n%10
#     r=r*10+d
#     n=n//10
# print(r)

# n=1234
# sum=0
# while n>0:
#     d=n%10
#     sum+=d
#     n=n//10
# print(sum)
n=[1,2,3,4,5,6]
# sum=[]
# for num in  n:
#     if num%2==0:
#      sum.append(num)
# print(sum)

# c=0
# for i in n:
#     if i%2==0:
#         c+=1
# print(c)


n=[10,20,2,3,99,44]
# l=n[0]
# for i in n:
#     if i > l:
#         l=i




# print(l)




# l=max(n)
# n.remove(l)
# s=max(n)
# print(s)




# l=second=float('-inf')
# for i in n:
#     if i>l:
#         second=l
#         l=i
#     elif i> second and i !=l:
#         second=i
# print(second)







# nums = [10, 45, 2, 99, 23]
# small=nums[0]
# for n in nums:
#     if n<small:
#         small=n
# print(small)



# num=int(input("enter the numbers"))
# if num<=1:
#     print("not prime")
# else:
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print("prime")
#     else:
#         print("not prime ")





# n=int(input("enter number :"))
# o=n
# rev=0
# while n>0:
#     d=n%10
#     rev=rev*10+d
#     n=n//10
# if o==rev:
#     print("paildrom")
# else:
#     print("not paildrown")

n=int(input("enter number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a , b =b,a+b
