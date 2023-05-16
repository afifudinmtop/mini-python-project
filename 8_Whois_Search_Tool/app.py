import whois


def perform_whois_lookup(address):
    try:
        w = whois.whois(address)
        return w.text  # Returns the WHOIS information as a string
    except Exception as e:
        return str(e)


def main():
    address = input("Enter an IP or host address: ")
    result = perform_whois_lookup(address)
    print(result)


if __name__ == "__main__":
    main()
