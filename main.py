# # function that takes in a list of numbers
# def square_numbers(nums):
#     # result variable which is set to an empty list
#     result = []
#     # looping through all the numbers from the list that we've passed in
#     for i in nums:
#         # appending each element in the list by multiplying it
#         result.append(i*i)
#     return result
#
# # passing in a list
# my_nums = square_numbers([1, 2, 3, 4, 5]) # resulting in [1, 4, 9, 16, 25]
# ----------------------------------------------------------------------------
# def square_numbers(nums):
#     for i in nums:
#         # 'yield' makes this function a generator
#         yield (i*i)

# # generators don't hold the entire result in memory /
# # they're waiting for us ask for the nex result
# my_nums = square_numbers([1, 2, 3, 4, 5])
# print(next(my_nums))

# # the for loop knows where to stop the iteration
# for num in my_nums:
#     print(num)
# -------------------------------------------------------------------------
# # list comprehension
# my_nums = [x*x for x in [1, 2, 3, 4, 5]]
my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)

for num in my_nums:
    print(num)
