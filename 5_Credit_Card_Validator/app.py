def validate_credit_card(number):
    # Step 1: Remove any spaces or hyphens from the input
    number = number.replace(' ', '').replace('-', '')

    # Step 2: Check if the input contains only digits
    if not number.isdigit():
        return False, ""

    # Step 3: Check if the length of the input is valid for credit card numbers
    if len(number) < 13 or len(number) > 16:
        return False, ""

    # Step 4: Determine the card type
    if number[0] == '4' and len(number) == 16:
        card_type = 'Visa'
    elif number[:2] in ['51', '52', '53', '54', '55'] and len(number) == 16:
        card_type = 'MasterCard'
    elif number[:2] in ['34', '37'] and len(number) == 15:
        card_type = 'American Express'
    elif number[:4] == '6011' and len(number) == 16:
        card_type = 'Discover'
    else:
        return False, ""

    # Step 5: Implement the Luhn algorithm for checksum validation
    digits = list(map(int, number))
    doubled_digits = [digits[i] * 2 if i % 2 ==
                      len(number) % 2 else digits[i] for i in range(len(digits))]
    summed_digits = [digit - 9 if digit >
                     9 else digit for digit in doubled_digits]
    total_sum = sum(summed_digits)
    if total_sum % 10 != 0:
        return False, ""

    # If all checks pass, the credit card number is valid
    return True, card_type


# Example usage
credit_card_number = input("Enter the credit card number: ")
valid, card_type = validate_credit_card(credit_card_number)
if valid:
    print("The credit card number is valid. Type: " + card_type)
else:
    print("The credit card number is invalid.")
