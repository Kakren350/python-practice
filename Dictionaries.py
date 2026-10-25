person = {
    "name": "Malcolm",
    "age": 27,
    "city": "Nanyuki",
    "favorite_food": "Mukimo"
}
print(person["name"])
print(person["favorite_food"])

person["hooby"] = "Football"
person["age"] = 30


for key, value in person.items() :
    print(f"{key}:{value}")


    