"""
1- lists *
2- dictionaries **
3- tuples ***
4- sets
"""

# ----------------------------------------------------------

# even_numbers = [0, "name", [1, 2], 6.0, 8, 10]
# print(even_numbers)

# even_numbers.append(12)
# print(even_numbers)

# even_numbers.extend([14, 16, 18])
# print(even_numbers)

# print(even_numbers.pop(6))
# print(even_numbers)
# # print(even_numbers[-1])


# print(even_numbers[2].pop(1))
# print(even_numbers[2])

# for i in even_numbers:
#     print(i)

# for i in range(0, len(even_numbers)):
#     print(i)

data_obj = {"name": "Ali", "age": 25, "organisation": "Venturenox"}

print(data_obj)
print(data_obj["name"])
print(data_obj["age"])

data_obj["designation"] = {"id": 1, "title": "front end"}

print(data_obj)
print(data_obj.keys())
print(data_obj.values())

# ------------------------------------------------------------------

test_tup = (1, 2, 3, 4)
print(test_tup)
test_tup[1] = 100

print(test_tup)
