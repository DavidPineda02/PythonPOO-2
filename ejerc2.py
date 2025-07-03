# 2. Mostrar el promedio de una secuencia de números (termina con 0). El usuario ingresa una secuencia de números y el programa calcula el promedio de los mismos.
# La secuencia termina con el ingreso del número 0.

class PromedioSecuencia:
    def __init__(self):
        """
        Constructor de la clase PromedioSecuencia.
        Inicializa una lista vacía para almacenar los números ingresados.
        """
        self.numeros = []  # Lista para almacenar los números ingresados

    def agregar_numero(self, numero):
        """
        Agrega un número a la lista de números.
        Parámetros:
            numero (int): Número a agregar.
        """
        self.numeros.append(numero)  # Agrega el número a la lista

    def calcular_promedio(self):
        """
        Calcula el promedio de los números ingresados.
        Retorna:
            float: Promedio de los números. Si no hay números, retorna 0.
        """
        if len(self.numeros) == 0:  # Verifica si la lista está vacía
            return 0  # Retorna 0 si no hay números para evitar división por cero
        return sum(self.numeros) / len(self.numeros)  # Calcula el promedio


# Programa principal
secuencia = PromedioSecuencia()  # Crea una instancia de la clase PromedioSecuencia

while True:  # Bucle para ingresar números
    try:
        numero_ingresado = int(input("Ingrese un número (0 para terminar): "))  # Solicita un número entero

        if numero_ingresado == 0:  # Si el usuario ingresa 0, termina el bucle
            break

        secuencia.agregar_numero(numero_ingresado)  # Agrega el número a la secuencia
    except ValueError:  # Captura errores si el usuario ingresa algo que no es un número entero
        print("Error: Ingrese solo números enteros.")  # Mensaje de error para entradas no válidas

promedio = secuencia.calcular_promedio()  # Calcula el promedio de los números ingresados
if promedio == 0:  # Verifica si no se ingresaron números
    print("No se ingresaron números para calcular el promedio.")  # Mensaje si no hay números
else:
    print(f"El promedio de los números ingresados es: {promedio:.2f}")  # Muestra el promedio con dos decimales
