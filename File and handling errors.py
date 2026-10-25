try:
    number = int(input("Enter a number: "))
    print("Valid number!")
    with open("numbers.txt", "a") as file:
        file.write(f"{number}\n")
except ValueError:
    print("Please enter a valid number. ")

with open("numbers.txt", "r") as file:
        print(file.read())

