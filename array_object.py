friends = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 25},
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 25},
]
for friend in friends:
    name = friend["name"]
    age = friend["age"]
    print("Name:", name.upper())
    print("Age:", age)