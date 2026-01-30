# Problem 9: Find average of numbers in a list
# Find and fix the error

numbers = [10, 20, 30, 40, 50]
if len(numbers) > 0:
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Average: {average}")
else:
    print("Cannot find average")