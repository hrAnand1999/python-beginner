# 🧠 What is a Dictionary?

# A dictionary in Python is an unordered, mutable collection of key–value pairs.

# Each key must be unique and immutable (like strings, numbers, or tuples),
# while values can be of any type (mutable or immutable).

# 🧩 Example:
student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science"
}

student1 = {
    1 : "Alice",
    2 : 21,
    3 : "Computer Science"
}
# print(student, student1)


# ✅ Keys: "name", "age", "course"
# ✅ Values: "Alice", 21, "Computer Science"

# ⚙️ 1️⃣ Creating a Dictionary

# There are several ways to create one:

# Using {}
# person = {"name": "John", "age": 25}

# Using dict() constructor
person = dict(name="John", age=25)
person['address'] = "123 Main St" # add new key-value pair

# print(person)

person["name"] = "Doe"  # update value for existing key

# print(person['rollNo']) # it will give error KeyError: 'rollNo'
# print(person.get('rollNo')) # it will give None

# Empty dictionary
empty_dict = {}

# 🔍 2️⃣ Accessing Values

# You can get values using their key:

student = {"name": "Alice", "age": 21}

# print(student["name"])  # Alice


# If you try to access a key that doesn’t exist:

# print(student["grade"])  # ❌ KeyError


# ✅ Use .get() to avoid errors:

# print(student.get("grade"))        # None
# print(student.get("grade", "N/A")) # N/A , we can provide default value

# ✍️ 3️⃣ Adding or Updating Elements
student = {"name": "Alice", "age": 21}

# Add a new key
student["grade"] = "A"

# Update an existing key
student["age"] = 22

# print(student)
# {'name': 'Alice', 'age': 22, 'grade': 'A'}

# ❌ 4️⃣ Removing Elements
# Method	Description	Example
# pop(key)	Removes and returns value	student.pop("age")
# popitem()	Removes last inserted item	student.popitem()
# del dict[key]	Deletes specific key	del student["grade"]
# clear()	Empties dictionary	student.clear()

# Example:

student = {"name": "Alice", "age": 21, "grade": "A"}
# print(student.pop("grade", "Not Found"))  # Not Found
# print(student.pop("age"))
# del student["age"]
# student.clear()
# print(student.popitem())
# print(student)  # {'name': 'Alice'}

# 📦 5️⃣ Looping Through a Dictionary
student = {"name": "Alice", "age": 21, "grade": "A"}

# Loop through keys
# for key in student:
    # print(key)

# Loop through values
# for value in student.values():
    # print(value)

# Loop through key-value pairs
# for key, value in student.items():
    # print(key, ":", value)


# ✅ Output:

# name : "Alice"
# age : 21
# grade : "A"

# 🧰 6️⃣ Dictionary Methods
# Method	Description	Example
# keys()	Returns all keys	student.keys()
# values()	Returns all values	student.values()
# items()	Returns key–value pairs	student.items()
# get(key)	Returns value if key exists	student.get("name")
# update()	Merges another dict	student.update({"city": "NY"})
# clear()	Empties the dictionary	student.clear()

# Example:

student.update({"age": 23, "city": "New York"})
# print(student)

# 🧮 7️⃣ Dictionary Comprehension

# Like list comprehensions, you can create dictionaries concisely.

# Square of numbers
squares = {x: x**2 for x in range(5)}
# print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 🧩 8️⃣ Nested Dictionaries

# You can store dictionaries inside dictionaries:

students = {
    "Alice": {"age": 21, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}


# print(students["Alice"]["grade"])  # A

# 🧾 9️⃣ Dictionary vs Other Data Structures
# Feature	Dictionary	List	Set	Tuple
# Stores Key-Value pairs	✅	❌	❌	❌
# Mutable	✅	✅	✅	❌
# Ordered (since Python 3.7+)	✅	✅	❌	✅
# Allows duplicate keys	❌	—	—	—
# 💡 10️⃣ Practical Examples
# Example 1: Counting Word Frequency
text = "apple banana apple orange banana apple"
words = text.split() # ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

count = {}
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1


print(len(count.keys()))
# {'apple': 3, 'banana': 2, 'orange': 1}

# Example 2: Mapping IDs to Users
users = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}
print(users[102])  # Bob

# 🧠 Summary Table
# Operation	Syntax	Example
# Create	{key: value}	{"a": 1}
# Access	dict[key] or dict.get(key)	d["a"]
# Add/Update	dict[key] = value	d["b"] = 2
# Delete	pop(), del, clear()	d.pop("a")
# Iterate	for k, v in dict.items()	loop through key-value pairs
# Check key	'key' in dict	'a' in d
# Copy	dict.copy()	new_d = d.copy()


# Problem 1: Create a dictionary of students and grades
# Example: students = {"Alice": 85, "Bob": 90} -> Output: {"Alice": 85, "Bob": 90}
students = {"Alice": 85, "Bob": 90}
print("Problem 1 Output:", students)

# Problem 2: Add a new student to the dictionary
# Example: Add "Charlie": 88 -> Output: {"Alice": 85, "Bob": 90, "Charlie": 88}
students["Charlie"] = 88
print("Problem 2 Output:", students)

# Problem 3: Print all keys and values
# Example: Output: Keys: ['Alice', 'Bob', 'Charlie'], Values: [85, 90, 88]
print("Problem 3 Output: Keys:", list(students.keys()))
print("Problem 3 Output: Values:", list(students.values()))

# Problem 4: Find average grade
# Example: Output: Average: 87.67
average = sum(students.values()) / len(students.keys()) if students else 0
print("Problem 4 Output: Average:", average)

# Problem 5: Check if a key exists in dictionary
# Example: Check "Bob" -> Output: True
key_to_check = "Bob"
exists = key_to_check in students
print(f"Problem 5 Output: Does '{key_to_check}' exist?", exists)
