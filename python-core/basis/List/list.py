tea_varities = ["Black", "Green", "Oolang", "white"]
print(tea_varities)
print(tea_varities[0])
print(tea_varities[-1])
print(tea_varities[2:])

tea_varities[3] = "herbal tea"
print(tea_varities)

tea_varities[1:2] = "Lemon"
print(tea_varities)

tea_varities = ["Black", "Green", "Oolang", "white"]
print(tea_varities)
print(tea_varities[1:2])

tea_varities[1:2] = ["Lemon"]
print(tea_varities)

print(tea_varities[1:3])

tea_varities[1:3] = ["green", "Masala"]
print(tea_varities)

print(tea_varities)

tea_varities[1:1] = ["test", "test"]
print(tea_varities)

tea_varities[1:3] = []
print(tea_varities)

for tea in tea_varities:
    print(tea)

for tea in tea_varities:
    print(tea, end="-")

if "Oolang" in tea_varities:
    print("I have Oolang tea")

tea_varities.append("Oolang tea")

print(tea_varities)

if "Oolang tea" in tea_varities:
    print("I havex Oolang tea")

print(tea_varities.pop())

tea_varities.remove("green")

print(tea_varities)

tea_varities_copy = tea_varities.copy()
tea_varities_copy.append("Lemon")

print(tea_varities_copy)
print(tea_varities)

squared_nums = [x**2 for x in range(10)]
print(squared_nums)

cube_nums = [y**3 for y in range(10)]
print(cube_nums)