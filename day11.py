# f = open("data.txt", "r")
# content = f.read()
# print(content)
# f.close()
# f=open("data.txt","w")
# f.write("python is good ")
# f.close()
# with open("note.txt","a")as f:
#     f.write("\n nani chowdary")
# # with open("note.txt","w") as f:
# #     f.write("Python File Handling Practice")
# with open("note.txt","r") as f:
#     print(f.read())
# Append your name
# with open("notes.txt", "w") as f:
#     f.write("Python File Handling Practice")
# with open("notes.txt", "a") as f:
#     f.write("\nKorapati Srinivasulu")  

# with open("notes.txt", "r") as f:
#     print(f.read())















# name=input("enter the name:")
# markes=input("enter marks:")
# with open("student.txt","a") as f:
#        f.write(name + " " + markes + "\n")
# print("/nAll student record:\n")
# with open ("student.txt","r") as f:
#        print(f.read())


while True:
    print("\n Student Record Manager")
    name=input("Enter the name :")
    marks=input("enter marks :")
    with open("student.txt","a") as f:
        f.write(name + " " + marks + "\n")
    choice=input("Add another student ? (yes/no):").lower()
    if choice !="yes":
        break
print("\n   All Student Record")
with open("student.txt","r") as f:
    print(f.read())