import random
import string


letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_chars = letters + digits + symbols
length, amount = 20, 10

for x in range(1, amount + 1):
    password = ''.join(random.sample(all_chars, length))
    print(f'{x}: {password}') # print(x,":",password)
    