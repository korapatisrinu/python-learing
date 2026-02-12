# 1.Write a program for sum of all the number in a list using for loop
# Ls=[45,12,32,65,98,12]
# sum=0
# for i in Ls:
#     sum=sum+i
#     print("sum of all number in list:",sum)







# 2. Find the number is odd or even using for loop.
# list1=(10,20,30,40,50 , 34, 22 , 25, 36,1,)
# for num in list1:
#     if num%2==0:
#         print(num,"is even number ")
#     else:
#         print(num,"is odd number")







# write a code below conditions: 

# 1.Generate a List with 20 random numbers between 10 and 50 
# 2. find second largest number in a list and second smallest number in a list
# import random
# num=[]
# for i in range(20):
#     n=random.randint(10,50)
#     num.append(n)
# print("List of random numbers:",num)
# num.sort()

# print("Second smallest number:",num[1])
# print("Second largest number:",num[-2])


























# # 4.  print Negative numbers in a list 
# list1 = [12, -7, 5, 64, -14] 
# # Output: -7, -14
# for num in list1:
#     if num < 0:
#         print(num)


















# 5. program to print all negative numbers in given range. 

# Input: start = -4, end = 5 
# Output: -4, -3, -2, -1
# start= -4
# end=5
# for num in range(start,end):
#     if num <0:
#         print(num)
























# 6. Count occurrences of an element in a list 

# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10] 
# x = 10 
# Output: 3 

# lst = [15, 6, 7, 10, 12, 20, 10, 28, 10] 
# x=10
# count=0
# for i in lst:
#     if i==x:
#         count+=1
# print("Occurrences of",x,"is:",count)












# 7. Remove empty List from List
 
# The original list is: [5, 6, [], 3, [], [], 9] -->input 
# List after empty list removal: [5, 6, 3, 9] -->output
# num = [5, 6, [], 3, [], [], 9]
# new_list=[]
# for i in num:
#     if i !=[]:
#         new_list.append(i)
# print("List after empty list removal:",new_list)













# 8.add a two list using for loop:
A=[10,12,15,45,30]
B=[18,38,16,82,20]
c=[]
# for i in range(len(A)):
#     c.append(A[i]+B[i])
# print("Addition of two list:",c)
for i in range(len(A)):
    s=A[i]+B[i]
    if s ==50:
        c.append(5)
    else:
        c.append(s)
print("Modified addition of two list:",c)