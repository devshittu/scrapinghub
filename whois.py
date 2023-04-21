import whois.whois.api.whois.api.
# w=whois.whois('appspot.com') 
w = whois.whois('appspot.com')
print(w.expiration_date)


print(w.text)