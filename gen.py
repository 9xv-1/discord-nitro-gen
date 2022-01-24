import random
import string

count = input("How many codes would you like to print?\n")

def get_code(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("https://discord.gift/" + result_str + "\n")


for i in range(int(count)):
    get_code(16)
