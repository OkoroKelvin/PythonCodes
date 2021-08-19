data = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f",
    },
    {
        "color": "cyan",
        "value": "#0ff"
    }

]
print("This is another method to solve the problem")
index = 1
for x in data:
    print("Index", index, "has", x.get("color"), "with value of", x.get("value"))
    index = index + 1
print()
print()
print()
print()

print("This is another method to solve the problem")
counter = 1
for item in data:
    print("Item", counter, "has", item["color"],"with value of", item["value"])
    counter +=1
print()
print()
print()
print()
print()
print()
print("This is another method to solve the problem")

for index, value in enumerate(data):
    print(f"Index{index} has {value['color']} with value of{value['value']}")
