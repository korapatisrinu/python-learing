# Find sum of list elements
# n=[10,20,30]
# t=0
# for i in n:
#     t+=i
# print("sum =",t)


# n=[10,30,40,50]
# l=n[0]
# for i in n:
#     if i>l:
#         l=i
# print("largest",l)
# Count even & odd numbers in a list
# n=list(map(int,input("enter the number:").split()))
# even=0
# odd=0
# for i in n:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("even=",even)
# print("odd=",odd)





# 7️⃣ Reverse a List
# num=[10,20,30]
# rev=[]
# for i in num:
#     rev.insert(0,i)
# print(rev)







# 8️⃣ Remove Duplicates from List
# n=[1,2,1,3,4,5,2,4,1]
# u=[]
# for i in n:
#     if i not in u:
#         u.append(i)
# print(u)




# n=[40,20,10,30]
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]>n[j]:
#             n[i],n[j]=n[j],n[i]
# print(n)


text = input("Enter a string: ").lower()

# # for ch in text:
# #     print(ch, end=" ")
# v=0
# c=0
# for ch in text:
#     if ch.isalpha():
#         if ch in "aeiou":
#             v+=1
#         else:
#             c+=1
# print(v)
# print(c)


if text =="":
    print("emty")
else:
    print("not emty")