class A:
    
    def __init__(self, name):
        self.__name = name
        
    def say_hello(self):
        return f'{self.__name} hello!'


class B(A):
    
    def get_name(self):
        return self._A__name
    
    def get_name2(self):
        return self.__class__.__bases__[0]


a = A('cat')
b =  B('dog')
print(b.get_name())

print(a.__dict__)
print(b.__dict__)