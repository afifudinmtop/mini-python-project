def caesar_cipher(message, key):
    encoded_message = ""

    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - ascii_offset + key) %
                               26 + ascii_offset)
            encoded_message += encoded_char
        else:
            encoded_message += char

    return encoded_message


def caesar_encode(message, key):
    return caesar_cipher(message, key)


def caesar_decode(message, key):
    # To decode the message, we need to subtract the key instead of adding it
    return caesar_cipher(message, -key)


# Example usage
message = "Hello There"
key = 8850

encoded_message = caesar_encode(message, key)
print("Encoded message:", encoded_message)

decoded_message = caesar_decode(encoded_message, key)
print("Decoded message:", decoded_message)
