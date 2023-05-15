import math


def calculate_pi(n):
    return round(math.pi, n)


# Get input from the user
num_decimal_places = int(
    input("Enter the number of decimal places to calculate PI (limit: 15): "))

# Limit the number of decimal places to 15
num_decimal_places = min(num_decimal_places, 15)

# Calculate and print PI
pi_value = calculate_pi(num_decimal_places)
print(f"PI (up to {num_decimal_places} decimal places): {pi_value}")
