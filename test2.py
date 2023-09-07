class Animal:
    def Walk(self, inDistance):
        print("Animal!")

class Cow(Animal):
    spots = 12
    
    def Walk(self, inDistance):
        Animal.Walk(inDistance)  # Gọi phương thức Walk của lớp cha Animal
        print("Spots "  " Distance " + str(inDistance))

test = Cow()
test.Walk(200)
