soda = {
    "Tonic": 2190,
    "Coke": 1250,
    "Sprite": 1290,
    "Fanta": 1200,
    "Diet_coke": 2250,
    "Stoney": 1340,
    "Krest": 790
}

for key, value in soda.items():
    print(f"{key}: {value}")

choice= input("Which soda do you want? ")

if choice in soda:
    print(f"price: {soda[choice]}")
    quantity = int(input("How many cases do you want? "))
    total = soda[choice] * quantity
    print(f"Total cost: {total}")
else:
    print("item not found")

    
# %%



Drinks = {
    "Tonic": 2190,
    "Coke": 1250,
    "Sprite": 1290,
    "Fanta": 1200,
    "Diet_coke": 2250,
    "Stoney": 1340,
    "Krest": 790
}   
def get_price(item_name):
    if item_name in Drinks:
        return Drinks[item_name]
    else:
        return None
choice = input("What Drinks do you want? ")
price= get_price(choice)

if price is not None:
    print(f"price: {price}")
else:
    print("item not found")

