#  Create a list with 2 integers,2 float ,2 string data
# data_list =[10,20,3.14,2.4,"nani","sreedhar"]
# print(data_list)



# . Create an Empty list
# empty_list=[]
# print(empty_list)




#  Data =[12,45,46,36,10.5,9.6]
# Replace 10.5 to 100

# data =[12,45,46,36,10.5,9.6]
# data[4]=100
# print(data)
# index=data.index(10.5)
# data[index]=100

# print(data)








#  Data=[10,12.5,’python’]
# Output: python Programming 
# 1.extract and remove python text from list
# 2.add ‘programming’ word with extracted word
# # 3.Finaly print the output
# data=[10,12.5,'python']
# extracted_word=data.pop(2)
# final_word=extracted_word + " Programming"
# print(final_word)
# Data=[12,45,2,78,36,92,101,9]
#  1.Print ascending order 
#  2.print descending order
# print("Ascending order:",sorted(Data))
# print("Descending order:",sorted(Data,reverse=True))











# Data=[12,45,63,78,95]
# # 1. Find and print the index value of 95 value
# index=Data.index(95)
# print("Index of 95:",index)















# 7. Create Dictionary with two key
# drict={"name":"sreedhar","age":25}
# print(drict)















# Add new key with this dict
#  dict1 = {'book': ['a', 'b', 'c'],
#  'age': [16,54,10]}
# Add new key:
#  Gender =[‘m’,’f’,’m’]
# dict1 = {'book': ['a', 'b', 'c'],
#     'age': [16, 54, 10]}
# dict1['gender'] = ['m', 'f', 'm']
# print(dict1)












# # Delete gender key from above dictionary
# dict1 = {'book': ['a', 'b', 'c'],
#     'age': [16, 54, 10],
#     'gender': ['m', 'f', 'm']}
# del dict1['gender']
# print(dict1)






















dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
marged_dict = dict1 | dict2
print(marged_dict)
