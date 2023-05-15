def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    elif n == 1:
        sequence = [0]
    elif n == 2:
        sequence = [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
    return sequence


# Example usage
number = int(input("Enter a number: "))
fib_sequence = fibonacci_sequence(number)
print(f"Fibonacci sequence up to {number}: {fib_sequence}")
