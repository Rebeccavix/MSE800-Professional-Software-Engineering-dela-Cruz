
class Singleton:

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            
        return cls._instance
        

a = Singleton()
b = Singleton()

print(id(a), id(b))


# class MyClass(Singleton):

#     def __init__(self, a):
#         self.a = a

#     def __str__(self):
#         return f"a is {self.a}"
    
# class_a = MyClass(10)
# print(class_a)
# class_b = MyClass(20)
# print(f"class_a is {class_a}, class_b is {class_b}")
