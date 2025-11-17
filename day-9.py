# 🔁 1. Basics of Loops in Python

# Python mainly has two loop types:

# ✅ A. for loop

# Used when you know what you are iterating over (sequence, range, collection).

# range generates a sequence of numbers: {0, 1, 2, 3, 4}

# for i in range(5):
#     print(i)

l = [1, 2, 3, 4, 5]

# if we use in inside loop, it will iterate through each element of the list l, and take the value of list

# for i in l:
#     print(i)

# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# for i in range(len(l)):
#     print(l[i])



# Output:

# 0 1 2 3 4

# ✅ B. while loop

# Used when you want to repeat something until a condition becomes False.

i = 0
# while i < 5:
#     print(i)
#     i += 1

# 🔄 2. Useful Loop Control Statements
# Keyword	Meaning
# break	Exit the loop immediately
# continue	Skip to next iteration
# pass	Do nothing (placeholder)

# Example:

# for i in range(5):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)

# 🧩 3. Looping through Different Data Types

# Now let’s see how loops work for each collection type in Python.

# 🍏 Looping through a List

# Lists maintain order and support indexing.

fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)


# With index:

# for i in range(len(fruits)):
#     print(i, fruits[i])


# Using enumerate (recommended): it returns both index and value

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# 🍇 Looping through a Tuple

# Same as lists (tuples are ordered & iterable):

t = (10, 20, 30)

# for x in t:
#     print(x)

# With index: 
# for i in range(len(t)):
#     print(i, t[i])

# 🌱 Looping through a Set

# Sets are unordered, so order of items is random.

s = {10, 20, 30, 10}

# for x in s:
#     print(x)


# ⚠️ You cannot use index (no s[0]). becuase sets are unordered collections.

# 📘 Looping through a Dictionary

# Dictionaries have key–value pairs.

# Loop through keys (default):
student = {"name": "Alice", "age": 21, "grade": "A"}

# for key in student:
#     print(key)   # just keys


# Explicit:


# for key in student.keys():
#     print(key)

# Loop through values:
# for value in student.values():
#     print(value)

# Loop through key–value pairs:
# for key, value in student.items():
#     print(key, value)

# 🔤 Looping through a String

# A string is a sequence of characters, so you can loop through it directly:

text = "python"

# for ch in text:
#     print(ch)

# 🧮 Looping with Range

# range() generates a sequence of numbers:

# range => 1st param: start (inclusive)
# range => 2nd param: end (exclusive)
# range => 3rd param: step (optional, default is 1)

# for i in range(1, 6):
#     print(i)


# Steps:

# for i in range(0, 10, 2):
#     print(i)

# 🧠 Summary Table
# Data Type	Ordered?	Loop Syntax	Supports Index?
# List	Yes	for x in list	Yes
# Tuple	Yes	for x in tuple	Yes
# Set	No	for x in set	No
# Dictionary	Yes (Python 3.7+)	for key, for value, for key, value	Keys only
# String	Yes	for ch in string	Yes


# Problem 1: Print numbers from 1 to 10
# Example: Output: 1 2 3 4 5 6 7 8 9 10
for i in range(1, 11):
    print(i, end=' ')
print()  # newline

# Problem 2: Print even numbers between 1 and 20
# Example: Output: 2 4 6 8 10 12 14 16 18 20
for i in range(2, 21, 2):
    print(i, end=' ')
print()

# Problem 3: Print right-angled triangle pattern
# Example: n = 5 -> Output:
# *
# **
# ***
# ****
# *****
n = 5
for i in range(1, n+1):
    print('*' * i)

# Problem 4: Print pyramid and inverted pyramid using '*'
# Example: n = 5 -> Output:
# Pyramid:
#     *
#    ***
#   *****
#  *******
# *********
# Inverted Pyramid:
# *********
#  *******
#   *****
#    ***
#     *
print("Pyramid:")
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
print("Inverted Pyramid:")
for i in range(n, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))

# Problem 5: Find sum of digits of a number
# Example: num = 1234 -> Output: 10
num = 1234
sum_digits = 0
for digit in str(num):
    sum_digits += int(digit)
print("Problem 5 Output:", sum_digits)
