Cars = {
    "Toyota": 200,
    "Mazda": 150,
    "Prado": 300,
    "Benz": 450,
    "Audi": 870,
    "Premio": 550

}
for key, value in Cars.items():
    print(f"{key}: {value}")

choice = input("Which car do you want? ")

if choice in Cars:
    print(f"Cars: {Cars[choice]}")
    quantity = int(input("How many do you want? "))
    total = Cars[choice] * quantity
    print(f"Total cost: {total}")
else:
    print("item not found")
