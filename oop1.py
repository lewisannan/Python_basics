class Dog:
    def __init__(self,name,breed,hasFur,):
        self.name = name
        self.breed = breed
        self.hasFur = hasFur

    def bark(self):
        print("Woof!! Woof!!")

    def locomotive(self):
        print("Dog is walking")

dog1 = Dog("Bill","Bulldog",True)
print(dog1.name,dog1.breed,"Does it have fur?",dog1.hasFur)
print()
dog1.locomotive()
dog2 = Dog("Milli","Chihuahua",False)
print(dog2.name,dog2.breed,dog2.hasFur)
print()
dog3 = Dog("Jill","German Shepherd",True)
print(dog3.name,dog3.breed,dog3.hasFur)
