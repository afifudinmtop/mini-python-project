import math


def calculate_e(n):
    return round(math.e, n)


# Get input from the user
num_decimal_places = int(
    input("Enter the number of decimal places to calculate e (limit: 15): "))

# Limit the number of decimal places to 15
num_decimal_places = min(num_decimal_places, 15)

# Calculate and print PI
e_value = calculate_e(num_decimal_places)
print(f"PI (up to {num_decimal_places} decimal places): {e_value}")
