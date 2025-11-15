import socket

def dns_lookup(domain):
    try:
        print(f"\n🔍 DNS Lookup for: {domain}")
        print("-" * 40)

        # A record (IPv4)
        ipv4 = socket.gethostbyname(domain)
        print(f"A Record (IPv4): {ipv4}")

        # getaddrinfo → multiple records
        print("\nAll DNS Records:")
        for result in socket.getaddrinfo(domain, None):
            print(result[4][0])

    except Exception as e:
        print("\n❌ Error:", e)


if __name__ == "__main__":
    domain = input("Enter domain name (example: google.com): ")
    dns_lookup(domain)
