# password generator 2
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÆØ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:._!@£$€&/=?``\\*+-"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 15
amount = 10

for i in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
