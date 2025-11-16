# 🧱 1️⃣ Tuples in Python
# 📘 What is a Tuple?

# A tuple is an ordered, immutable (unchangeable) collection of items.
# It can contain elements of different data types.

# Creating a tuple
numbers = (1, 2, 3)
person = ("Alice", 25, "Engineer")
mixed = (10, "Python", 3.14)
tup = tuple([1, 2, 3])


# ✅ Characteristics:

# Ordered → Elements have a fixed position (can be accessed by index)

# Immutable → Cannot be changed after creation

# Allows duplicates

# 🧩 Tuple Examples
t = (1, 2, 3, 4, 5)

# t[0] = 10  # This will raise an error because tuples are immutable
# Access elements
# print(t[0])   # 1
# print(t[-1])  # 5

# Length of tuple
# print(len(t))  # 5

# Slicing
# print(t[1:4])  # (2, 3, 4)

# ⚙️ Tuple Methods

# Tuples have very few methods because they are immutable:

t = (1, 2, 3, 2, 3) 

# print(t.count(2))  # 2 → counts how many times 2 appears
# print(t.index(3))  # 2 → position of value 3

# 🧠 Why Use Tuples?

# To store fixed data (e.g., coordinates, dates)

# Faster than lists (since they are immutable)

# Can be used as keys in dictionaries (because they are hashable)

# Example:

location = (40.7128, -74.0060)
# cities = {location: "New York"}
# print(cities)

# 📌 Tuple Packing and Unpacking
# Packing
person = ("Alice", 25, "Engineer")


# Unpacking
name, age, profession = person
name = person[0]
age = person[1]
profession = person[2]
# print(name)       # Alice
# print(profession) # Engineer
# print(person)

# 🔷 2️⃣ Sets in Python
# 📘 What is a Set?

# A set is an unordered, mutable collection of unique items.

# Creating a set
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 3, 2}
num2 = set([1, 2, 2, 3])

print(numbers)  # {1, 2, 3} → duplicates removed
print(num2)


# ✅ Characteristics:

# Unordered → No indexing or slicing

# Mutable → You can add or remove elements

# No duplicates

# 🧩 Set Examples
# Creating an empty set
s = set()  # NOT s = {}, which creates a dictionary

# Adding elements
s.add(10)
s.add(20)
print(s)  # {10, 20}

# Removing elements
s.remove(10)
s.discard(20)  # does not raise error if element missing

# Check membership
print(30 in s)

# ⚙️ Set Operations (Very Powerful)

# Sets are great for mathematical operations 👇

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union → {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection → {3, 4}
print(a - b)  # Difference → {1, 2}
print(a ^ b)  # Symmetric difference → {1, 2, 5, 6}

# 🧠 Why Use Sets?

# To remove duplicates from a list quickly:

nums = [1, 2, 2, 3, 3, 4] 
unique_nums = set(nums)
print(unique_nums)  # {1, 2, 3, 4}


# For fast membership tests (sets are optimized for lookups):

print(3 in unique_nums)  # True


# For mathematical set operations (union, intersection, etc.)

# 🧩 3️⃣ Tuple vs Set — Key Differences
# Feature	Tuple	Set
# Syntax	(1, 2, 3)	{1, 2, 3}
# Ordered	✅ Yes	❌ No
# Mutable	❌ No	✅ Yes
# Duplicates Allowed	✅ Yes	❌ No
# Indexing/Slicing	✅ Yes	❌ No
# Hashable (can be dict key)	✅ Yes	❌ No
# Use Case	Fixed ordered data	Unique, unordered data
# 🧮 Example Comparison
# Tuple example
point = (10, 20)
print(point[0])  # 10

# Set example
ids = {101, 102, 103, 101}
print(ids)  # {101, 102, 103}

# 🧾 Summary
# Concept	Tuple	Set
# Type	Ordered Collection	Unordered Collection
# Mutable?	❌ No	✅ Yes
# Allows Duplicates?	✅ Yes	❌ No
# Use Case	Fixed structured data (coordinates, records)	Unique items, set operations
# Common Methods	count(), index()	add(), remove(), union(), intersection()

# ✅ In short:

# Use a tuple when you need ordered, fixed data.

# Use a set when you need unique, unordered data or set operations.

# Problem 1: Create a tuple of fruits and print the first item
# Example: fruits = ("apple", "banana", "cherry") -> Output: "apple"
fruits = ("apple", "banana", "cherry")
print("Problem 1 Output:", fruits[0])

# Problem 2: Create a set of numbers and add a new one
# Example: numbers = {1, 2, 3}; add 4 -> Output: {1, 2, 3, 4}
numbers = {1, 2, 3}
numbers.add(4)
print("Problem 2 Output:", numbers)

# Problem 3: Find intersection and union of sets
# Example: a = {1, 2, 3}, b = {2, 3, 4} -> Intersection: {2, 3}, Union: {1, 2, 3, 4}
a = {1, 2, 3}
b = {2, 3, 4}
print("Problem 3 Output: Intersection:", a & b)
print("Problem 3 Output: Union:", a | b)

# Problem 4: Remove duplicates from list using set
# Example: nums = [1, 2, 2, 3, 3, 3] -> Output: [1, 2, 3]
nums = [1, 2, 2, 3, 3, 3]
unique_nums = list(set(nums))
print("Problem 4 Output:", unique_nums)

# Problem 5: Convert tuple to list and back
# Example: fruits = ("apple", "banana") -> list: ["apple", "banana"] -> tuple: ("apple", "banana")
fruits_tuple = ("apple", "banana")
fruits_list = list(fruits_tuple)
fruits_tuple_again = tuple(fruits_list)
print("Problem 5 Output: List:", fruits_list)
print("Problem 5 Output: Tuple:", fruits_tuple_again)
