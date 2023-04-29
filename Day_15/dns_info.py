import dns
import dns.resolver

result = dns.resolver.resolve('osintme.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())
