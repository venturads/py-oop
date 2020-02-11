#python object-oriented programming

class User:

    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies
        print("Welcome new hire: ", self.name, ", age: ", self.age)
        
kobe = User("Kobe", 41, ['basketball', 'movies'])
shaq = User("Shaq", 55, ['food', 'donuts'])
#print("Welcome new hire: {}, age: {} ".format(kobe.name, kobe.age))
