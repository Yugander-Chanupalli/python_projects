import requests
import sys
import pyfiglet

Banner=pyfiglet.figlet_format("sub-enum tool")
print(Banner)

wordlist_location = input("Enter the wordlist_location:").strip()
sub_file = open(wordlist_location, 'r')
sub_list = sub_file.readlines()
sub_list = [word.strip() for word in sub_list]

for sub in sub_list:
    sub_domain = f'https://{sub}.{sys.argv[1]}'

    try:
        requests.get(sub_domain)
    except requests.ConnectionError:
        pass
    else:
        print("valid domain:",sub_domain)