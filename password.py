import secrets
import string
import random

letters = string.ascii_letters
print(letters)

digits = string.digits
print(digits)

special_chars = string.punctuation
print(special_chars)

selection_list = letters + digits + special_chars
print(selection_list)

password_len = 20

password = ''
for i in range(password_len):
    password+= ''.join(secrets.choice(selection_list))


f = open("password.txt", "w")
f.write(password)
f.close()
