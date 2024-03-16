def operacion(cantidad, balance, tipo="deposito"):


    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None
    
    if tipo == "deposito":
        return deposito(cantidad, balance)
    
    elif tipo == "retiro":
        return retiro(cantidad, balance)
        
resultado = operacion(10, 30, "retiro")
print(resultado)

"""
Básicamente explicó que podemos usar funciones dentro de funciones, aunque según mi manera de pensar
no fue el mejor ejemplo que pudo haber dado.
"""