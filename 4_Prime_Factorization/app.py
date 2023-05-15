def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_factorization(number):
    factors = []
    i = 2
    while i <= number:
        if number % i == 0:
            if is_prime(i):
                factors.append(i)
                number //= i
            else:
                i += 1
        else:
            i += 1
    return factors


# Get input from the user
num = int(input("Enter a number: "))

# Find prime factors
prime_factors = prime_factorization(num)

# Display the prime factors
if prime_factors:
    print("Prime factors:", prime_factors)
else:
    print("The number has no prime factors.")
