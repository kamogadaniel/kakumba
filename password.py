

import random

print("Your password: ")

chars = "gwsdfyuawtg4rc348957y23?@:~"

password = " "
for x in range(16):
    password += random.choice(chars)

print(password)