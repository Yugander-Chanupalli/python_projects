import requests
import pyfiglet
import sys

Banner=pyfiglet.figlet_format("Dictionary-Brute_Force")
print(Banner)

location=input("Enter the location of wordlist:")
with open(location,'r') as word_file:
    wordlist=word_file.readlines()
wordlist=[word.strip() for word in wordlist]

Valid_Domain=[]


for word in wordlist:
    domain=f'https://{sys.argv[1]}/{word}'

    try:
        response=requests.get(domain)
    except requests.ConnectionError:
        pass
    if response.status_code==200:
        Valid_Domain.append(domain)


print("Valid Domains:",Valid_Domain)
