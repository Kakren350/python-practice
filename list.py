food = ["Ugali","Rice","Chapati","Githeri","Matoke"]
print(food[0])
print(food[-1])
print(len(food))

food.append("Samosa")
food.remove("Rice")
food[0] = "Meat"

print(food)

for index, item in enumerate(food) :
    print(f"{index+1}.{item}")