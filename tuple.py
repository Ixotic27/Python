#Duck typing- in python object type doesnt matter if an object has the required method than python allows it

class Dog:
    def sound(self):
        print("Bark") 

class cat:
    def sound(self):
        print("Meow")

def animal_sound(obj):
    obj.sound()

animal_sound(Dog())
animal_sound(cat())