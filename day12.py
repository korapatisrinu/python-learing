# try:
#     num=int(input("enter the number:"))
#     print(num)
# except ValueError:
#     print("Invalid input! Please enter an integer.")
# try:
#     a=int(input("enter the frist :"))
#     b=int(input("enter the second :"))
#     r= a/b
#     print(r)
#     print("its dived ")
# except ZeroDivisionError:
#     print("cannot divdied by zero")
    
# except ValueError:
#     print("Invalid input.")




# try:
#     marks=int(input("enter the marks :"))
#     if marks >100:
#         raise ValueError("Marks cannot be greater than 100!")
#     print("marks accted:",marks)
# except ValueError as e:
#      print(" Error:", e)








class Animals:
    def sound(self):
        print("Animal makes sound")
class Dog(Animals):
    def sound(self):
        print("Dog barks")
d1=Dog()
d1.sound()
