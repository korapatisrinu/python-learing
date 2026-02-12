# 1 Find Highest Number (Unique)
# Given numbers, remove duplicates and print highest number.
# If list empty → print -1.
# n = int(input())
# nums = list(map(int, input().split()))

# # unique_nums = list(set(nums))

# if n== 0:
#     print(-1)
# else:
#     print(max(set(nums)))






#  2Find Third Highest Unique Number
# Given numbers, remove duplicates and print third highest number.
n= int(input().strip())
nums=list(map(int,input().split()))
unique_nums=list(set(nums))
if len(unique_nums)<3:
    print(-1)
else:
    unique_nums.sort(reverse=True)
    print(unique_nums[2])
