# class Account:
#     def __init__(self,balance):
#         self.__balance=balance
#     def dispoit(self,amount):
#         self.__balance+=amount
#         print("Deposited",amount)
#         print("New balance:",self.__balance)
#     def withdraw(self,amount):
#         if amount >self.__balance:
#             print("Insufficient balance")
#         else:
#             self.__balance-=amount
#             print("withdraw",amount)
#     def show_balance(self):
#         print("Current Balance:",self.__balance)
# acc=Account(5000)
# acc.dispoit(2000)
# acc.withdraw(3000)
# acc.show_balance()











# 🟡 Task 2 — Class Variable

# Create class Student with:

# class variable → school_name

# instance variable → student_name



# class Student:
#     school_name="narayana english medium school"
#     def __init__(self,student_name):
#         self.student_name=student_name
# s1=Student("nani")
# s2=Student("sreedhar")
# print("student1:",s1.student_name,"-",Student.school_name)
# print("student2:",s2.student_name,"-",Student.school_name)














# 🔵 Task 3 — Static Method

# Create class Converter with:

# Static method:

# celsius_to_fahrenheit(c)


# Formula:

# F = (C × 9/5) + 32


# Use @staticmethod





# class Converter:
#     def celsius_to_fahrenheit(c):
#          f = (c *9/5) + 32
#          return f
# result=Converter.celsius_to_fahrenheit(25)
# print("Temperature in Fahrenheit:", result)









# 🟢 LEVEL 1 — Encapsulation Practice
# 1️⃣ Create class User

# Private attributes:

# __username

# __password

# Methods:

# set_password(pwd)

# check_password(pwd) → returns True/False
# class User:
#     def __init__(self,username):
#         self.__username=username
#         self.__password=""
#     def set_password(self,pwd):
#         self.__password=pwd
#         print("password set succefully")
#     def check_password(self,pwd):
#         if pwd==self.__password:
#            return True
#         else:
#             return False
# u1=User("nani")
# u1.set_password("1234")
# print(u1.check_password("1234"))
# print(u1.check_password("0000"))








# class Wallet:
#     def __init__(self,balance):
#         self.__balance=balance
#     def add_money(self,amount):
#         self.__balance+=amount
#         print("ADD AMOUNT",amount)
#         print("new balance",self.__balance)
#     def spend_money(self,amount):
#         if amount>self.__balance:
#             print("Not enough money")
#         else:
#             self.__balance-=amount
#             print("spendmoney",amount)
#             print("remaing balance",self.__balance)
#     def show_balance(self):
#         print("currenytblance:",self.__balance)
# w1=Wallet(2000)
# w1.add_money(500)
# w1.spend_money(300)
# w1.show_balance()







# class Employee:
#         company_name = "Infosys"
#         def __init__(self,name,salary):
#                 self.name=name
#                 self.salary=salary
#         def dispay(self):
#                 print("Company ",Employee.company_name)
#                 print("name:",self.name)
#                 print("salary:",self.salary)
# e1=Employee("nani",45000)
# e2=Employee("srinu",50000)
# e1.dispay()
# print("_________--------------")
# e2.dispay()        



# class Book:
#     total_books=0
#     def __init__(self,name):
#         self.name=name
#         Book.total_books+=1
#         print("Total books created:", Book.total_books)
# b1=Book("python")
# b2=Book("java")
# b3=Book("api")






# class MathHelper:
#     @staticmethod

#     def square(x):
#         return x*x
#     @staticmethod

#     def cube(x):
#          return x*x*x
#     @staticmethod

#     def even(x):
#        return x%2==0
# print("Square:", MathHelper.square(4))
# print("Cube:", MathHelper.cube(3))
# print("Is Even:", MathHelper.even(10))
# print("Is Even:", MathHelper.even(7))



# 🔴 LEVEL 4 — Mixed Advanced (Interview Level)
# 7️⃣ Create class Bank

# Private:

# __balance

# Class variable:

# bank_name

# Methods:

# deposit()

# withdraw()

# show_balance()

# Static method:

# bank_policy() → prints bank rules

# class Bank:
#     bank_name="SBI"
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount <=0:
#             return "Amount must be positive"
#         self.__balance+=amount
#         print(f"doispoted:{amount}")
#         print(f"new balace:{self.__balance}")
#     def withdraw(self,amount):
#         if amount>=self.__balance:
#             print(" Insufficient balance")
#         else:
#             self.__balance-=amount
#             print("withdraw:",amount)
#             print("remainging balance:",self.__balance)
#     def show_balance(self):
#             print("current balance:",self.__balance)
#     @staticmethod
#     def bank_policy():
#             print("Bank Policy: Maintain minimum balance of 1000")
# b1=Bank(5000)
# print("Bank name:",Bank.bank_name)
# b1.deposit(2000)
# b1.withdraw(2000)
# b1.show_balance()
# Bank.bank_policy()













# /---------------------------ATM------------------------------------------------------------
class ATM:
    def __init__(self,pin,balance=0):
        self.__pin=pin
        self.__balance=balance
    def check_pin(self):
        enter_pin=input("Enter your ATM pin:")
        return enter_pin==self.__pin
    def deposit(self):
        amount=int(input("Enter the amount :"))
        if amount<=0:
             print("Invalid amount")
             return
        self.__balance+=amount
        print(f"✅ Deposited: {amount}")
    def withdraw(self):
        amount=int(input("Enter the amount to withdraw: "))
        if amount>=self.__balance:
             print("❌ Insufficient balance")
        elif amount<=0:
            print("Invalid amount")
        else:
            self.__balance-=amount
            print(f"✅ Withdrawn: {amount}")
    def show_balance(self):
         print(f"💰 Current balance: {self.__balance}")
atm=ATM(pin="0120",balance=50000)
if atm.check_pin():
    while True:
        print("\n====== ATM MENU ======")
        print("1.Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            atm.deposit()
        elif choice=="2":
            atm.withdraw()
        elif choice=="3":
            atm.show_balance()
        elif choice=="4":
             print("🙏 Thanks for visiting ATM")
             break
        else:
            print("Invalid choice")
else:
    print("❌ Wrong PIN")
