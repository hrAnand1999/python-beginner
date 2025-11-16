# Arithmetic Operators in Python
# | Operator | Description         | Example   | Result |
# | -------- | ------------------- | --------- | ------ |
# | `+`      | Addition            | `5 + 3`   | `8`    |
# | `-`      | Subtraction         | `10 - 4`  | `6`    |
# | `*`      | Multiplication      | `2 * 6`   | `12`   |
# | `/`      | Division (float)    | `10 / 4`  | `2.5`  |
# | `//`     | Floor Division      | `10 // 4` | `2`    |
# | `%`      | Modulus (remainder) | `10 % 3`  | `1`    |
# | `**`     | Exponentiation      | `2 ** 3`  | `8`    |


# Comparison Operators in Python
# | Operator | Description              | Example  | Result  |
# | -------- | ------------------------ | -------- | ------- |
# | `==`     | Equal to                 | `5 == 5` | `True`  |
# | `!=`     | Not equal to             | `5 != 3` | `True`  |
# | `>`      | Greater than             | `7 > 5`  | `True`  |
# | `<`      | Less than                | `3 < 8`  | `True`  |
# | `>=`     | Greater than or equal to | `5 >= 5` | `True`  |
# | `<=`     | Less than or equal to    | `4 <= 2` | `False` |

# Logical Operators in Python
# | Operator | Description                                    | Example              | Result  |
# | -------- | ---------------------------------------------- | -------------------- | ------- |
# | `and`    | Returns True if both conditions are True       | `(x > 5 and y > 10)` | `True`  |
# | `or`     | Returns True if at least one condition is True | `(x > 5 or y < 5)`   | `True`  |
# | `not`    | Reverses the condition                         | `not(x > 5)`         | `False` |

# Assignment Operators in Python
# | Operator | Description             | Example   | Equivalent To |
# | -------- | ----------------------- | --------- | ------------- |
# | `=`      | Assign value            | `x = 5`   | —             |
# | `+=`     | Add and assign          | `x += 3`  | `x = x + 3`   |
# | `-=`     | Subtract and assign     | `x -= 2`  | `x = x - 2`   |
# | `*=`     | Multiply and assign     | `x *= 4`  | `x = x * 4`   |
# | `/=`     | Divide and assign       | `x /= 2`  | `x = x / 2`   |
# | `//=`    | Floor divide and assign | `x //= 3` | `x = x // 3`  |
# | `%=`     | Modulus and assign      | `x %= 2`  | `x = x % 2`   |
# | `**=`    | Exponent and assign     | `x **= 3` | `x = x ** 3`  |


import math
print(math.ceil(10/4))

a = 2
b = 5

print(a ** b)

a = 5
b = 5
c = 4
d = 4
if a == b or c == d:
    print("a is not equal to b")
else:
    print("a is equal to b")

if not(a == b) and c == d:
    print("a is not equal to b")
else:
    print("a is equal to b")

a = 5
b = 10
print(a, b)
# a = a + 2
a += 2
# python uses the left hand value and increment by right hand value and assing it to left hand value
print(a, b)

# b = b - 3
b -= 3
print(b)

# a = a * 2
a *= 2
print(a)

# a = a / 2
a //= 2
print(a)

# a = a % 3
# a %= 3
# print(a)

# a = a ** 7
a **= 7
print(a)


# problem = both statement should be true for and operator to return true
# problem = either statement should be true for or operator to return true


# aur (hindi mei ) = and
# ya (hindi mei) = or