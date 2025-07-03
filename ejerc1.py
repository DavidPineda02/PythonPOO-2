# 1. Determinar si un número es perfecto. El usuario ingresa un número y el programa indica si es perfecto o no.
# Un número es perfecto si la suma de sus divisores propios es igual al número.

class NumeroPerfecto:
    def __init__(self, numero):
        """
        Constructor de la clase NumeroPerfecto.
        Inicializa el número a evaluar.
        Parámetros:
            numero (int): Número que se desea verificar.
        """
        self.numero = numero  # Almacena el número ingresado

    def es_perfecto(self):
        """
        Determina si el número es perfecto.
        Retorna:
            bool: True si el número es perfecto, False en caso contrario.
        """
        if self.numero <= 0:  # Verifica si el número es menor o igual a cero
            return False  # Los números negativos o cero no pueden ser perfectos

        suma_divisores = 0  # Inicializa la suma de los divisores propios

        for i in range(1, self.numero):  # Itera sobre todos los números desde 1 hasta self.numero - 1
            if self.numero % i == 0:  # Verifica si i es un divisor propio del número
                suma_divisores += i  # Suma el divisor a la variable acumuladora

        return suma_divisores == self.numero  # Retorna True si la suma de divisores es igual al número


try:
    # Solicita al usuario que ingrese un número
    numero = int(input("Ingrese un número: "))
    num_obj = NumeroPerfecto(numero)  # Crea una instancia de la clase NumeroPerfecto con el número ingresado

    if num_obj.es_perfecto():  # Llama al método es_perfecto para verificar si el número es perfecto
        print(f"{numero} es un número perfecto.")  # Muestra un mensaje si el número es perfecto
    else:
        print(f"{numero} no es un número perfecto.")  # Muestra un mensaje si el número no es perfecto

except ValueError:  # Captura errores si el usuario ingresa algo que no es un número entero
    print("Error: Ingrese solo números enteros positivos.")  # Mensaje de error para entradas no válidas 
