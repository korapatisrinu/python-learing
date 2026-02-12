# Division by Zero
# try:
#     a=5
#     b=0
#     print(a/b)
# except ZeroDivisionError:
#   print("Error: Division by zero is not allowed.") 















# 2. Invalid Input



# try:
#     n=int(input("enter a number:"))
#     print(n)
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")





















# 3. String to Integer Conversion

# try:
#     x=int("abc")
#     print(x)
# except ValueError:
#     print("Error: Invalid string to integer conversion.")







# File Not Found
# try:
#   f=open("text.txt", "r")
# except FileNotFoundError:
#   print("Error: File not found.")

















# 5. List Index Error
# try:
#     list1=[1,2,3]
#     print(list1[5])
# except IndexError:
#     print("Error: List index is out of range.")












# . Try – Except – Else
# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("error")
# else:
#     print("division successful")
















# 7. Try – Except – Finally
# try:
#     print(10/0)
# except:
#     print("error")
# finally:
#     print("done")















# 8. Multiple Exceptions
# try:
#     a = int(input("Enter number: "))
#     print(10 / a)
# except ValueError:
#     print("Invalid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

















# 9. Dictionary Key Error
# try:
#     my_dict ={"key1":1,"key2":2,}
#     print(my_dict["key1"])
# except KeyError:
#     print("Error: Key not found in dictionary.")








# n = int(input().strip())
# scores = list(map(int, input().split()))

# unique_scores = list(set(scores))

# if len(unique_scores) < 2:
#     print(-1)
# else:
#     unique_scores.sort(reverse=True)
#     print(unique_scores[1])




# n=int(input().strip())
# scores=list(map(int,input().split()))
# un_scroes=list(set(scores))
# if len(un_scroes)<2:
#    print(-1)
# else:
#    un_scroes.sort(reverse=True)
#    print(un_scroes[1])




















# n = int(input().strip())
# s = input().strip()

# prev = 0
# curr = 1
# ans = 0

# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         curr += 1
#     else:
#         ans += min(prev, curr)
#         prev = curr
#         curr = 1
# ans = max(ans, min(prev, curr))
# print(ans * 2)


import pandas as pd 
df=pd.read_csv("C:\\Users\\nanic\\Downloads\\Cars_Data.csv")
