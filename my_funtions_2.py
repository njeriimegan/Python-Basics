def add(x, y, z):
    return x + y + z


def addition(*numbers):  # *-any number of arguments
    # total = sum(numbers)
    total = 0
    for num in numbers:
        total = total + num
    return total


# save(age=18, dob='2001-12-31', professional='Doctor', gender='Female')
def save(**data):  # kwargs
    with open("values.txt", "a") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")


# save(dob='2012-06-14', gender='female', name='Blessing')
# for k,v (_,v) in data.items():
# print(item)

def some_function(name, *scores, **details):
    pass


def cylinder(r, h):
    # documentation of a function """"""
    """
    Calculates the volume and surface area of a cylinder
    :params:
     :r: radius of the cylinder
     :h: height of the cylinder
     :return: volume and surface area
    """
    v = 22 / 7 * r * r * h
    sa = 22 / 7 * r * r * 2 + 22 / 7 * r * 2 * h
    return sa, v


surf_area, volume = cylinder(7, 60)  # _ ignores the value
print(surf_area, volume)

# some_function("Kamau", 60, 42, 90, gender="male", course="Chem")


# print(addition(90, 89,49, 56, 32, 17, 200))
# print(addition(21, 49))

# result = add(1, 2, 3)
# print(result)


# lambda functions

divider = lambda x, y : x/y

area_circle = lambda radius: 22/7 * radius * radius

print(divider(45, 7))
res = area_circle(59)
print(res)
