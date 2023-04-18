# Question 1
# Write a function to print "hello_USENAME!" USERNAME is the input of the function. 

# def hello_name(user_name):
    
#         print("hello_" + user_name.upper() + "!")

# hello_name("username")








# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing



# def first_odds():
#     numbers= range(0,100)
#     for number in numbers:
#         if number % 2 != 0:
#             print (number)
# first_odds()







# Question 3
# Plese write a Python function, max_num_in_list to return the max number of a given list. 

# def max_num_in_list(a_list):
#     max = a_list [0]
#     for num in a_list:
#         if num > max:
#             max = num
#     return max

# print(max_num_in_list([45,-9,8675,3,66]))




# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false)

# def is_a_leap_year (a_year):
#     if a_year % 4 == 0 and a_year % 100 != 0:
#         return True
#         if a_year % 100 != 0:
#             return False
#     if a_year % 400 == 0:
#                  return True
#     else:
#         return False

# print(is_a_leap_year(1900))




# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 


# def is_consecutive(a_list):
#     index = 0
#     pointer = a_list[0]
#     for test in a_list:
#         if test == pointer + index:
#             index += 1
#         else:
#             return False
#     return True
# print(is_consecutive([2,3,4,5,6,7]))


    





