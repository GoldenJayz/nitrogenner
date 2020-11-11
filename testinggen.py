import random
import string
import os

os.system("cls")

BLUE = "\033[0;34m"
BOLD = "\033[1m"
YELLOW = "\033[1;33m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
FAINT = "\033[2m"

print('Created by: GoldenJayz')
amount = int(input('How much nitro codes do you wish to generate?:\n'))
f = open('output.txt', 'w')

for i in range(amount):
    code = "https://discordapp.com/gifts/%s" % (('').join(random.choices(string.ascii_letters + string.digits, k=16)))
    print(code, file=f) 
    print(code)
