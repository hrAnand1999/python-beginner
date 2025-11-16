# 🧠 What is a List?

# A list is an ordered, mutable (changeable) collection of items — it can hold elements of different data types.

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
emptyList = []

# print(fruits, numbers, mixed, emptyList)


# ✅ Lists are written with square brackets [ ]
# ✅ They maintain insertion order (since Python 3.7)

# 🧩 1. Creating Lists
empty_list = []
numbers = [10, 20, 30]
names = list(('abc', 'def', 'ghi', 1))  # using list() constructor
# print(names)

# 🔢 2. Accessing Elements

# Use indexing (0-based):

fruits = ["apple", "banana", "cherry"]

# print(fruits[0])   # apple
# print(fruits[-1])  # cherry (last element)

# ✂️ 3. Slicing Lists

# Get a portion (sublist) using list[start:end] — end is excluded.

nums = [10, 20, 30, 40, 50] 

# print(nums[1:4])  # [20, 30, 40] in string second param is lenght, whereas in list its index, and print end index - 1
# print(nums[:3])   # [10, 20, 30]
# print(nums[2:])   # [30, 40, 50]
# print(nums[-3:])  # [30, 40, 50]

# ➕ 4. Adding Elements
# Method	Description	Example
# append(x)	Add one item at the end	fruits.append("orange")
# insert(i, x)	Add item at index i	fruits.insert(1, "mango")
# extend(iterable)	Add multiple items	fruits.extend(["grape", "kiwi"])

# Example:

nums = [1, 2, 3]
nums.append(4)       # [1, 2, 3, 4]
nums.insert(1, 10)   # [1, 10, 2, 3, 4]
nums.extend([5, 6])  # [1, 10, 2, 3, 4, 5, 6]

# ➖ 5. Removing Elements
# Method	Description	Example
# remove(x)	Removes first occurrence of value	fruits.remove("apple")
# pop(i)	Removes item at index (default last)	fruits.pop(1)
# clear()	Removes all items	fruits.clear()

# Example:

nums = [1, 2, 3, 4, 3]
# nums.remove(3)  # [1, 2, 4, 3]
# nums.pop(3)      # [1, 2]
nums.clear()    # []

# print(nums)

# 🔄 6. Updating Elements

# Lists are mutable, so you can reassign elements:

nums = [10, 20, 30]
nums[1] = 200
# print(nums)  # [10, 200, 30]

# 🧮 7. Useful List Operations
# Operation	Example	Output
# len(lst)	len([1,2,3])	3
# sum(lst)	sum([1,2,3])	6
# min(lst)	min([5,1,9])	1
# max(lst)	max([5,1,9])	9
# sorted(lst)	sorted([3,1,2])	[1,2,3]
# in	2 in [1,2,3]	True


# 🔁 8. Iterating Over a List
nums = [10, 20, 30]
for n in nums:
    print(n)


# With index:

for i, n in enumerate(nums):
    print(i, n)

# 🧰 9. List Comprehensions

# A Pythonic way to create new lists.

squares = [x*x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]


# With condition:

even = [x for x in range(10) if x % 2 == 0]
print(even)  # [0, 2, 4, 6, 8]

# 🪄 10. Copying Lists
a = [1, 2, 3]
b = a.copy()       # creates a shallow copy
b.append(4)

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]


# Avoid b = a — that points to the same list in memory.

# 🧩 11. Nested Lists (2D Lists)

# You can store lists inside lists:

matrix = [[1, 2],
           [3, 4],
             [5, 6]]
# print(matrix[1][0])  # 3

# matrix2 = matrix.copy() # shallow copy
import copy
matrix2 = copy.deepcopy(matrix)
print(matrix2)
print(matrix)
matrix2[1][0] = 99
print("After modifying matrix2:")
print(matrix)
print(matrix2)



# Problem 1: Create a list of movies and print 2nd item
# Example: movies = ["Inception", "Interstellar", "Tenet"] -> Output: "Interstellar"
movies = ["Inception", "Interstellar", "Tenet"]
if len(movies) >= 2:
    print("Problem 1 Output:", movies[1])
else:
    print("Problem 1 Output: Not enough movies")

# Problem 2: Add and remove elements from a list
# Example: Add "Dunkirk", remove "Tenet" -> Output: ['Inception', 'Interstellar', 'Dunkirk']
movies.append("Dunkirk")
if "Tenet" in movies:
    movies.remove("Tenet")
print("Problem 2 Output:", movies)

# Problem 3: Sort numbers ascending
# Example: numbers = [5, 2, 9, 1] -> Output: [1, 2, 5, 9]
numbers = [5, 2, 9, 1]
sorted(numbers)
print("Problem 3 Output:", numbers)

# Problem 4: Find sum of all elements in a list
# Example: numbers = [5, 2, 9, 1] -> Output: 17
print("Problem 4 Output:", sum(numbers))

# Problem 5: Find max, min and average of a list
# Example: numbers = [5, 2, 9, 1] -> Output: max=9, min=1, avg=4.25
max_num = max(numbers)
min_num = min(numbers)
avg_num = sum(numbers) / len(numbers) if numbers else 0
print(f"Problem 5 Output: max={max_num}, min={min_num}, avg={avg_num}")
