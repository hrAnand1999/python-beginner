# 🧠 What is a String?

# A string is a sequence of characters enclosed in quotes — used to store text.

name = "Alice"
greeting = 'Hello'


# ✅ Both single ' and double " quotes work the same in Python.

# 🧩 1. Creating Strings

# You can create strings in multiple ways:

str1 = 'Hello'
str2 = "World"
str3 = '''This is
a multiline
string.'''
# print(str1, str2, str3)


# 📝 Triple quotes (''' or """) let you write multiline strings.

# 🔤 2. Accessing Characters

# Strings are indexed, meaning each character has a position (starting at 0).

text = "Python"

# print(text[0])   # 'P'
# print(text[1])   # 'y'
# print(text[-1])  # 'n' (last character)

# 🔁 3. Slicing Strings

# You can extract parts (substrings) using slicing syntax:
# string[start:end] → includes start, excludes end.

text = "Python"

# print(text[0:3])  # 'Pyt'
# print(text[2:])   # 'thon'
# print(text[:4])   # 'Pyth'
# print(text[-3:])  # 'hon'

# ➕ 4. String Concatenation and Repetition

# Join or repeat strings easily:

first = "Hello"
second = "World"

print(first + ' ' + second)  # 'Hello World'
print(first * 3)             # 'HelloHelloHello'

# 📏 5. String Length

# Use the len() function to find the number of characters:

text = "Python"
print(len(text))  # 6

# index = length of string - 1

# 🔡 6. String Methods (Common Ones)

# Strings have many built-in methods:

s = "  hello world  I am Python  "

print(s.upper())       # '  HELLO WORLD  '
print(s.lower())       # '  hello world  '
print(s.title())       # '  Hello World  '
print(s.strip())       # 'hello world'  (remove side spaces)
print(s.replace("world", "Python"))  # '  hello Python  '
print(s.split())       # ['hello', 'world']  (splits by space)


# 👉 You can chain methods:

print(s.strip().title())  # 'Hello World'

# 🔍 7. Checking Substrings
s = "Python is fun"

print("Python" in s)    # True
print("Java" not in s)  # True

# 🧮 8. String Formatting

# You can insert variables into strings in several ways.

# ✅ a) f-Strings (Python 3.6+)
name = "Alice"
age = 25
print(f"My name is {name}, and I am {age} years old.")

# ✅ b) format() method
print("My name is {}, and I am {} years old.".format(name, age))

# ✅ c) Old style (%)
print("My name is %s, and I am %d years old." % (name, age))

# 🔢 9. Escape Characters

# Special characters start with a backslash (\):

# Escape	Meaning	Example
# \'	Single quote	'It\'s fine'
# \"	Double quote	"She said \"Hello\""
# \\	Backslash	"C:\\path\\file.txt"
# \n	New line	"Hello\nWorld"
# \t	Tab	"A\tB\tC"
# 🧱 10. Raw Strings

# Use r"" to ignore escape sequences (useful for file paths):

path = r"C:\new_folder\test.txt"
print(path)


# ✅ Output:

# C:\new_folder\test.txt


# Problem 1: Print the 3rd character of a name
# Example: name = "Anand" -> Output: "a"
name = "Anand"
if len(name) >= 3:
    print("Problem 1 Output:", name[2])
else:
    print("Problem 1 Output: Name too short")

# Problem 2: Replace spaces with underscores in a string
# Example: text = "Hello World" -> Output: "Hello_World"
text = "Hello World"
print("Problem 2 Output:", text.replace(' ', '_'))

# Problem 3: Take name input and say Hello
# Example: Input: "Anand" -> Output: "Hello, Anand!"
user_name = input("Enter your name: ")
print(f"Problem 3 Output: Hello, {user_name}!")

# Problem 4: Count vowels in a string
# Example: text = "Python" -> Output: 1
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in s:
        if i in vowels:
            count = count + 1
    return count

sample_text = "Python"
print("Problem 4 Output:", count_vowels(sample_text))

# Problem 5: Reverse a string without using [::-1]
# Example: text = "Python" -> Output: "nohtyP"
def reverse_string(s):
    result = ''
    for char in s:
        result = char + result
    return result

sample_text2 = "Python"
print("Problem 5 Output:", reverse_string(sample_text2))
