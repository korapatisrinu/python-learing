# . Check whether a given number is positive, negative, or zero.
# Sample Input: n = -7
# Sample Input: n = 0
# n=-7
# if n>0:
#     print("Positive")
# elif n<0:
#     print("Negative")
# else:
#     print("Zero")



# 2. Check whether a number is even or odd.
# Sample Input: n = 24
# Sample Input: n = 19
# n=int(input("Enter a number: "))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")







# Check whether a person is eligible to vote (age >= 18)
# age=int(input("enter your age:"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")








# . Find the greater of two numbers
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# if a>b:
#     print("a")
# else:
#     print("b")











# . Find the greater of three numbers
# a = 10
# b = 55
# c = 33
# if a>=b and a>=c:
#     print("a is greater")
# elif b>=a and b>=c:
#     print("b is greater")
# else:
#     print("c is greater")
# check whter given year leap year or not
# year=int(input("enter year:"))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print("leap year")
# else:
#     print("not leap year")
















#  Check whether a character is a vowel or a consonant.
# ch=input("enter a character:")
# if ch.lower() in 'aeiou':
#     print("vowel")
# else:
#     print("consonant")








#  Check whether a given number is divisible by 5 and 11.
# n=int(input("enter a number:"))

# if n%5==0 and n%11==0:
#     print("divisible by 5 and 11")
# else:
#     print("not divisible by 5 and 11")




#  Calculate grade based on marks: 90+ = A, 75–89 = B, 50–74 = C, below 50 = Fail.
# marks=89
# if marks>=90:
#     print("A")
# elif marks>=75:
#     print("B")
# elif marks>=50:
#         print("C")
# else:
#     print("Fail")




















#  Check whether a given character is uppercase, lowercase, or a digit.
# ch=input("enter a character:")
# if ch.isupper():
#     print("uppercase")
# elif ch.islower():
#     print("lowercase")
# elif ch.isdigit():
#     print("digit")
# else:
#     print("special character")













# Check whether a number lies between 10 and 50 (inclusive)
# n=int(input("enter a number:"))
# if 10<=n<=50:
#     print("number lies between 10 and 50")
# else:
#     print("number does not lie between 10 and 50")








# Check whether a number is single-digit, double-digit, or multi-digit.
# n=int(input("enter a number:"))
# if -9<=n<=9:
#     print("single-digit")
# elif-99<=n<=99:
#     print("double-digit")
# else:
#     print("multi-digit")













# 13. Check whether a triangle is valid based on three angle values (sum = 180 and each > 0)
# a=60
# b=60
# c=60
# if a>0 and b>0 and c>0 and a+b+c==180:
#     print("valid triangle")
# else:
#     print("not a valid triangle")


















# 4. Classify temperature as Cold (<15), Warm (15–30), or Hot (>30).
# temp=25
# if temp<15:
#     print("Cold")
# elif 15<=temp<=30:
#     print("Warm")
# else:
#     print("Hot")







#  Calculate electricity bill based on units: Units <100 = 2/unit, 100–300 = 3/unit, >300 = 5/unit
units=250
if units<100:
    bill=units*2
elif 100<=units<=300:
    bill=units*3
else:
    bill=units*5
print("Electricity Bill:", bill)

