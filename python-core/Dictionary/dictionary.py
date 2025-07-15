chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types["Masala"])

print(chai_types.get("gingery"))

chai_types["Green"] = "Fresh"

print(chai_types)

for chai in chai_types:
    print(chai, chai_types[chai])


for key, value in chai_types.items():
    print(key, value)


if "Masala" in chai_types:
    print("I have masala chai")

print(len(chai_types))
print(chai_types)

chai_types = {"Earl Grey" : "Citrus"}
print(chai_types)

chai_types.pop("Earl Grey")
print(chai_types)
