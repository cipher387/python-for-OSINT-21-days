import whois 

whois_info = whois.whois('sector035.nl')

print (whois_info)

print("Creation date")

print(whois_info["creation_date"])
