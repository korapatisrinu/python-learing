# students={
#     "id":101,
#     "name":"srinu",
#     "couruse":"python",
#     "city":"gudur"
# }
# print("keys:")
# for key in students.keys():
#     print(key)
# print("\nvalues:")
# for values in students.values():
#     print(values)




# text=input("enter the name:")
# feru={}
# for ch in text:
#     if ch in feru:
#         feru[ch]+=1
#     else:
#         feru[ch]=1
# print(feru)


# word=input("enter the word:")
# f={}
# for words in word:
#     if words in f:
#         f[words]+=1
#     else:
#         f[words]=1
# print(f)


# marks={
#     "maths":67,
#     "python":56,
#     "sql":77
# }
# t=0
# for m in marks.values():
#     t+=m
# a=t/len(marks)
# print(t)
# print(a)

# 6️⃣ Check whether a key exists in dictionary
# student = {
#     "id": 101,
#     "name": "Srinu",
#     "course": "Python"
# }

# key = input("Enter key to check: ")

# if key in student:
#     print("Key exists")
# else:
#     print("Key does not exist")
# 1️⃣ Create a dictionary for employee details
em={
    "id": 101,
    "name": "Ravi",
    "designation": "Developer",
    "salary": 45000,
    "city": "Hyderabad"
}
for key,value in em.items():
    print(key, ":",value)