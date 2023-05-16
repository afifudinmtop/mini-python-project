import requests


def get_country_from_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    country = data.get('country')
    return country


def get_public_ip():
    url = 'http://ip-api.com/json'
    response = requests.get(url)
    data = response.json()
    ip_address = data.get('query')
    return ip_address


# Prompt the user for an IP address or use the public IP automatically
user_ip = input("Enter an IP address (press enter to use your public IP): ")
if user_ip == "":
    user_ip = get_public_ip()

# Call the function to get the country from the IP address
country = get_country_from_ip(user_ip)

# Print the result
if country:
    print(f"The IP address {user_ip} is registered in {country}.")
else:
    print("Could not find the country for the specified IP address.")
