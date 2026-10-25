



    
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
      

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

    def have_birthday(self):
        self.age = self.age + 1
        print(f"Happy birthday {self.name}! You are now {self.age}")    


Dennis = Person("Dennis", 27)


Dennis.introduce()
Dennis.have_birthday()
Dennis.introduce()