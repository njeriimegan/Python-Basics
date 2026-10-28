import math


def greet():
    # name = input("Enter your name: ")
    print("hello there")

def greeting(user):
    print(f"hello {user}, karibu sana")

def area_of_a_circle(radius, precision=3):# optional param
    a = 22/7 * radius * radius
    result = round(a, precision)
    print(result)


def volume_of_a_cylinder(r, h):
    v = 22/7 * r**2 * h
    return v

print(volume_of_a_cylinder(8.5, 12.8))

result = volume_of_a_cylinder(8, 29.6)
print(round(result))

# # named params
# area_of_a_circle(precision=2, radius=11)

# positional params
# area_of_a_circle(9, 1)
# area_of_a_circle(8.97, 3)
# area_of_a_circle(8)
# greet() #calling == using
# greet()

# params or args
# greeting("Mso")
# greeting("Wesley")