# # Function to Find Largest of 3 Numbers
# def lagest_check(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# print(lagest_check(10,25,15))
# def vowel_count(s):
#     c=0
#     for ch in s.lower():
#         if ch in "aeiou":
#            c+=1
#     return c
# print(vowel_count("python programming"))


def rev_list(s):
    return s[::-1]
n=[1,2,3,4,5]
print(rev_list(n))