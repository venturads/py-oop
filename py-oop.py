#python object-oriented programming

class User:

    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

kobe = User("Kobe", 41, ['basketball', 'movies'])

print("Welcome new hire: {}, age: {} ".format(kobe.name, kobe.age))
