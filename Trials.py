Cars = ["Mazda","Prado","Harrier","Benz","Toyota"]
print(Cars [0])
print(Cars [-1])
Cars [0] = "Bentley"
print(len(Cars))

Cars.append("Audi")
Cars.remove("Bentley")

print(Cars)

for index, item in enumerate (Cars) :
    print(f"{index+1}.{item}")




age = int(input("What's your age? "))
has_id_input= input("Do you have an ID? yes/no ")
if age >=20 and has_id_input == "yes" :
    print("You can drink beer")
else:
    print("You can not drink beer") 


name= input("What's your name? ")
age = int(input("What's your age? "))
print(f"{name} will be {age+5} in 5 years")
