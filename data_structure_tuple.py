"""
Data Structure in Python:
هياكل البيانات في البايثونّ
    * List  ليست
    > Tuples  تيوبليس
    * Dic  ديكشنريس
    * sets  سيت
    * Frozensets فروزن سيت
"""


"""
2. Tuples

Methods in tuples:
    * count
    * index
"""

# create tuple
# nums = ()

# or
# nums = tuple()
# or
nums = 1,2,3,'Yes', True, 'Yes',
# (0,1,2,3,4)
# show type of data
print(type(nums))

# loop data
for number in nums:
    print(number)


print(nums.count('Yes'))