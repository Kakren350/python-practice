class Drink:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
            if quantity <= self.stock:
                self.stock -= quantity
                return self.price * quantity
            else:
                print("Not enough stock")
                return None
            
shop = {
    "coke": Drink("Coke", 1250, 10),
    "sprite": Drink("Sprite", 1290, 5)
}  
while True: 
    for drink in shop.values():
           print(f"{drink.name}: {drink.price} (stock: {drink.stock})")

    choice = input("Which drink? (or 'quit' to exit) ").strip().lower()
    if choice == "quit":
              break
    if choice not in shop:
              print("Not found") 
              continue
    try:
              quantity = int(input("How many? "))
    except ValueError:
              print("Please enter a valid number")
              continue
    result = shop[choice]. sell(quantity)
    if result is not None:
           print(f"Total cost: {result}")
           with open ("sales_log.txt", "a") as file:
                      file.write(f"Sold {quantity} {choice} for {result}\n")
          


    



             
            


        