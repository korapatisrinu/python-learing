# Task 1

# Create a class Car with:

# brand

# model

# Add method display() to print details.



# class car:
#     def __init__(self,brand,modle):
#         self.brand=brand
#         self.modle=modle
#     def display(self):
#         print("car brand:",self.brand)
#         print("car modle:",self.modle)
# car1=car("BMW","INvov")
# car1.display()
   












# class BankAccount:
#     def __init__(self,Account_holder,balance):
#         self.Account_holder=Account_holder
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print("Deposited:", amount)
#         print("New Balance:", self.balance)
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance-=amount
#             print("Withdrawn:", amount)
#             print("Remaining Balance:", self.balance)
# amount1=BankAccount("nanichowdary",5000)
# amount1.deposit(2000)
# amount1.withdraw(3000)
# amount1.withdraw(1000)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def geek(self):
#         print(f"Hi,my self {self.name} and i am {self.age} years old")
# p1=Person("nani",21)
# p1.geek()





# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def average(self):
#         avg=sum(self.marks)/len(self.marks)
#         return avg
#     def highest_mark(self):
#         return max(self.marks)
# p1=Student("nani",[100,90,90,95,90,95])
# print("Avarage Marks:",p1.average())
# print("highest_mark:",p1.highest_mark())



# class Vehicle():
#     def __init__(self,brand):
#         self.brand=brand
#     def start(self):
#         print("Vehicle started")
# class Car(Vehicle):
#     def __init__(self,brand,modle):
#         super().__init__(brand)
#         self.modle=modle
#     def display(self):
#         print("car brand:",self.brand)
#         print("car modle:",self.modle)
# c1=Car("BMW","i8")
# c1.start()
# c1.display()

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dog barks")

# d1 = Dog()
# d1.sound()

# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dog barks")
# d1=Dog()
# d1.sound()



class ShoppingCart:
    def __init__(self):
        self.items={}

    def add_items(self,name,price):
        self.items[name]=price
        print(f"{name} add with price {price}")
    def remove_items(self,name):
        if name in self.items:
                del self.items[name]
                print(f"{name} remove from cart")
        else:
             print("item is not found")
    def total_price(self):
         total=sum(self.items.values())
         return total
    

cart = ShoppingCart()
cart.add_items("Shirt", 1200)
cart.add_items("Shoes", 2500)
cart.add_items("Watch", 3000)

cart.remove_items("Shoes")

print("Total Price:", cart.total_price())