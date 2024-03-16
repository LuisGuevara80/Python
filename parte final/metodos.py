class Circulo:

    pi = 3.141592

    @classmethod
    def area(cls, radio):    # Por convensión, como queremos que este método, sea un método de clase. El parametro tendrá por nombre cls
        return cls.pi * (radio ** 2)

resultado = Circulo.area(14)
print(resultado)