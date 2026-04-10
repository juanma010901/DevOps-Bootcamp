def suma(a, b):
    #Retorna la suma de 2 numeros
   
    #Parameters:
    # a (int):Un numero aleatorio.
    # b (int):Un numero aleatorio.

    #Returns
    # suma(int):La suma de los numeros ingresados.
    return a + b

def resta(a, b):
    #Retorna la resta de 2 numeros

    #Parameters:
    # a (int):Un numero aleatorio.
    # b (int):Un numero aleatorio.
    # resta(int):La resta de los numeros ingresados.
    return a - b

def multiplicacion(a, b):
    # Retorna la multiplicación de 2 números

    # Parameters:
    # a (int/float): Un número.
    # b (int/float): Un número.
    # Returns:
    # int/float: El resultado de la multiplicación.

    return a * b

def division(a, b):
    # Retorna la división de 2 números

    # Parameters:
    # a (int/float): Un número.
    # b (int/float): Un número (no debe ser 0).
    # Returns:
    # float: El resultado de la división.

    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    return a / b
