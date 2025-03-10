import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%^&*()_+{}[]."

all_characters = lower + upper + numbers + symbols
length = 12

password = "".join(random.sample(all_characters, length))
print(password)
