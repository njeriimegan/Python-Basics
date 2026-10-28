import random

import my_functions

with open("data.txt", "a") as file:
#     # file.write("99\n")
#     # file.write("68\n")
    for temp in range(100):
        x = random.randint(-10, 100)
        file.write(str(x)+"\n")
#
with open ("data.txt", "r") as file:
    content = (file.read()) #0params 0args
    print(content)

# number =random.randint(1,10)
# print(number)

my_functions.greet()