import string
import random

characters = list(string.ascii_letters + string.digits + ".")
length = int(input("How many characters do you want in your password: "))
random.shuffle(characters)
password = []
for i in range(length):
    password.append(random.choice(characters))
random.shuffle(password)
print("".join(password))