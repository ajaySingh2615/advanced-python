# determine if a fruit is ripe, overripe, or unripe, based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "banana"
color = "yellow"

if fruit == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "overripe":
        print("Brown")

else:
    print("Please we don't have any information regarding to this fruit")