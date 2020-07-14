my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
    "dad": {
        "name": "John",
        "age": 72
    }
}


for key, value in my_family.items():
    print(f"{value['name']} is my {key} and is {value['age']} years old")


