class A:
    def __init__(self, name):
        self.__name = name
        
    def say_hello(self):
        return f'{self.__name} hello!'


class B(A):
    #def __init__(self, name):
        #self.__name = name
    
    def get_name(self):
        return self.__name


a = A('cat')
b =  B('dog')


print(a.__dict__)
print(b.__dict__)