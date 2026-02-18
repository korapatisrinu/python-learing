# import csv
# with open("employeep.csv","w",newline="") as f:
#     writer=csv.writer(f)
#     writer.writerow(["Name","Salary"])
#     writer.writerow(["nani",80000])
#     writer.writerow(["ram",20000])
#     writer.writerow(["srinu",2000])

# with open("employeep.csv","r")as f:
#     reader=csv.reader(f)
#     for row in reader:
#         print(row)

import json
data={
"name":"nani",
"age":22,
"skills":["python","java"]
}
with open("data.json","w")as f:
    json.dump(data,f)
with open("data.json","r") as f:
    data=json.load(f)
    print("Name:", data["name"])
print("Age:", data["age"])
print("Skills:", data["skills"])