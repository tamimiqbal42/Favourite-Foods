# print("hello")

class Person:
    def __init__(self, name, age, hight=5.7):
        self.nam = name
        self.a = age
        self.hi = hight
    
    def __str__(self):
        return f"My name is {self.nam}.I am {self.a} years old"
    
    def myfunc(self, nai):
        self.nai = nai
        print(f"Hello my name is {self.nai} but {self.nam} name dake !!!")
        
obj = Person("Tamim", 21)
obj.myfunc("Tamim Iqbal Khan")

print(obj.nam)
print(obj.a)
print(obj.hi)
print(obj)
