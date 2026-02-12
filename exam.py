 

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




# # 22️⃣ Write a function to count vowels in a string
# def cout(n):
#     v='aeiouAEIOU'
#     count=0
#     for ch in n:
#         if ch in v:
#             count+=1
#     return count
# text=input("enter name")
# print(cout(text))
# x = 5
# y = 2
# print(x // y)














# n = int(input("Enter a number: "))
# print(check_even_odd(n))

# def even_odd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# num=int(input("enter the number:"))
# print(even_odd(num))








# def lagrest_number(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# print(lagrest_number(10,25,1))



# def vowel_count(s):
#     c=0
#     for ch in s.lower():
#         if ch in "aeiou":
#            c+=1
#     return c
# print(vowel_count("python programming"))











# impti 
# n = list(map(int, input("Enter numbers separated by space: ").split()))
# r=[]
# for num in n:
#     if num!=0:
#         r.append(num)
# zero_count=n.count(0)
# for i in range(zero_count):
#     r.append(0)
# print(r)












# Create a dictionary for a student with:

# name

# roll

# marks

# Then print all key–value pairs using a loop.



# students={
#     "name":"nani",
#     "roll":22,
#     "marks":299
# }
# for key,value in students.items():
#     print(key,":",value)
# n=[10,20,3,50,90]
# frist=0
# for i in n:
#     if i>frist:
#         frist=i
# print(frist)
# n=in

# def rev(s):
#     word=s.split()
#     word=word[::-1]
#     return " ".join(word)
# print(rev("python ai engineer"))










# num=[1,2,2,3,4,4,5]
# unique=[]
# for i in num:
#     if i  not in unique:
#         unique.append(i)
# print(unique) 





# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# for i in range(8):
#     print(fibonacci(i),end=" ")
# nums = [5, 12, 7, 18, 3, 20]
# s={x:"Even" if x%2==0 else "odd" for x in  nums}
# print(s)
# nums = [1,2,3]
# print(nums.append(4))


# def count(s):
#     word=s.split()
#     return len(word)
# test="python is very powerful language"
# print(count(test))
# nums = [10, 20, 4, 45, 99]

# nums.sort()
# print(nums[-2])
n=[1,2,3,4,5,6,7,8,9,10]
s=[x**2 for x in n if x%2==0]
print(s)