salary = int(input("Enter your salary: "))

if salary >= 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus =", bonus)