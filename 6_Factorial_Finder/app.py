def factorial_loop(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# Example usage
number = int(input("Enter a positive integer: "))
result = factorial_loop(number)
print(f"The factorial of {number} is: {result}")
