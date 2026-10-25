def salary (days_worked, price_per_days):
    return days_worked*price_per_days
result = salary(28,250)
print(f"Total cost: {result}")

# %%
soda = {
    "Tonic": 2190,
    "Coke": 1250,
    "Sprite": 1290,
    "Fanta": 1200,
    "Diet_coke": 2250,
    "Stoney": 1340,
    "Krest": 790
}
def get_price(item_name):
    if item_name in soda:
        return soda[item_name]
    else:
        return None

choice = input("What soda do you want? ")
price = get_price(choice)

if price is not None:
    print(f"price: {price}")
else:
    print("item not found")    
