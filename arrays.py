#list
people = ["Kasim", "Kivuva", "Karen", "Kwepo", "Katule"]
scores = [78, 90, 49, 56, 79, 61, 42, 39]

# print(people[0])
# print(scores[-1]) #last value
#
people.append("Kalonzo")
# print(people)
# scores.append(89)
# print(scores)

# people.sort()
# scores.sort(reverse=True)
# print(people)
# print(scores)
# people.append("Kaleche")
# people.append("Kawala")
# print(people)
#
# print (people[0], scores[-1])
# print(sum(scores) / len(scores))
# print(len(scores))

scores.sort()
print(scores[-3:]) #slicing
print(scores[:3])

print(scores[3:5])

# set-removes duplicates
numbers = {3, 9, 60, 70, 70, 89}
print(numbers)

# Tuple - immutable data
days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(days[5])

# dictionary key + Value
person = {"name": "Zion", "city": "Mandera", "age": 34}
print(person["name"])

watu = [{"name": "Dumsula", "city": "Mandera", "age": 34}, {"name": "Kavise", "city": "Marsabit", "age": 24}, {"name": "Paulo", "city": "Kakamega", "age": 40}]
print(watu[2]["age"])
