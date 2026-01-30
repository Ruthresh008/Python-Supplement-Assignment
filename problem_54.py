# Problem 54: Find nth Fibonacci number
# Find and fix the error

def nth_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

print(f"10th Fibonacci number: {nth_fibonacci(10)}")
