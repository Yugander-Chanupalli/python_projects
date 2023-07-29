import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hash Cracker")
print(ascii_banner)

print("Available hash algorithms are: MD5 | sha256")
hash_type = str(input("Enter the type of algorithm: "))
wordlist_location = str(input("Enter the location of the file: "))
user_hash = str(input("Enter the hash: "))

#with open(wordlist_location, 'r') as wordlist_file:
  #  word_list = wordlist_file.read().splitlines()
wordlist_file = open(wordlist_location, 'r')
word_list = wordlist_file.readlines()
word_list = [word.strip() for word in word_list]  # Strip leading/trailing whitespaces

for word in word_list:
    if hash_type == "MD5":
        hash_object = hashlib.md5(word.encode("utf-8"))
        hashed = hash_object.hexdigest()
        if user_hash == hashed:
            print(f'\033[1;32m HASH FOUND: {word}\n')
    elif hash_type == "sha256":
        hash_object = hashlib.sha256(word.encode("utf-8"))
        hashed = hash_object.hexdigest()
        if user_hash == hashed:
            print(f'\033[1;32m HASH FOUND: {word}\n')
    else:
        print("HASH NOT FOUND")
