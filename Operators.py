# Input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic Operators
print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison Operators
print("\nComparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical Operators
print("\nLogical Operators")
print("(a > 0 and b > 0):", a > 0 and b > 0)
print("(a > 0 or b > 0):", a > 0 or b > 0)
print("not(a > b):", not(a > b))

# Assignment Operator
print("\nAssignment Operator")
c = a
c += b
print("c += b :", c)

# Bitwise Operators
print("\nBitwise Operators")
print("a & b :", a & b)
print("a | b :", a | b)
print("a ^ b :", a ^ b)
print("~a :", ~a)
print("a << 1 :", a << 1)
print("a >> 1 :", a >> 1)

# Expression
result = (a + b) * 2
print("\nExpression Result:", result)