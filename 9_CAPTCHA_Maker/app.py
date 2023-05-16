import random
from PIL import Image, ImageDraw, ImageFont

# Generate a random string of alphanumeric characters


def generate_random_string(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    captcha = ''.join(random.choices(characters, k=length))
    return captcha

# Generate a CAPTCHA image with the given text


def generate_captcha_image(text, width, height, font_path, font_size):
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), text, font=font, fill=(0, 0, 0))
    return image

# Save the CAPTCHA image to a file


def save_captcha_image(image, file_path):
    image.save(file_path)


# Example usage
captcha_text = generate_random_string(6)
captcha_image = generate_captcha_image(captcha_text, 200, 100, 'arial.ttf', 36)
save_captcha_image(captcha_image, 'captcha.png')
