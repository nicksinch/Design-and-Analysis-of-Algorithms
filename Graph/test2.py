class ExampleClass:

    l = []

    def __init__(self, p):
        self.__p = p
        self.l.append(1)

    def set_p(self, s):
        self.__p = s
    
    
v = ExampleClass(2)
print(v.l)
v2 = ExampleClass(3)
print(v2.l)

print(v.__p)