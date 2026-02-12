# 1️⃣ Reverse a string
# name=input("enter  your name:")
# rev=""
# for ch in name:
#     rev=  ch  + rev
# print(rev)


# palindrome check
n=input("enter the name ")
# if n==n[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


# Count vowels in a string
# n=input("enter the name :")
# count=0
# for ch in n.lower():
#     if ch in 'aeiou':
#         count+=1
# print("Count vowels ",count)

v=0
c=0
for ch in n.lower():
    if ch.isalpha():
     if ch in 'aeiou':
        v+=1
     else:
        c+=1
print(v)
print(c)