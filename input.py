# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing calculations
sum_result = num1 + num2
difference = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Displaying results
print("\nResults:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
