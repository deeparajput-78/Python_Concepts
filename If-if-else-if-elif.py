# Conditional Statements in Python
# Examples of if, if-else, and if-elif-else

print("===== IF Statement =====")
age = 20

if age >= 18:
    print("You are eligible to vote.")

print("\n===== IF-ELSE Statement =====")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

print("\n===== IF-ELIF-ELSE Statement =====")
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F (Fail)")