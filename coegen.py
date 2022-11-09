class CoeGen:
    def __init__(self, tamano: int = 16, ancho: int = 8) -> None:
        self.datos = []
        self.tamano = self.minmax(tamano, 16, 65536)
        self.ancho = self.minmax(ancho, 1, 1024)
        self.maximo = int(2**self.ancho) - 1

    def generar_coe(self):
        with open('datos.coe', mode='w', encoding='utf-8') as archivo:
            archivo.write('memory_initialization_radix = 2;\n')
            archivo.write('memory_initialization_vector =\n')
            for i in range(self.tamano):
                if len(self.datos) > 0:
                    dato = self.datos.pop()
                else:
                    dato = 0
                dato_bin = self.dec_a_bin(dato)
                if i == (self.tamano - 1):
                    archivo.write(f'{dato_bin};')
                else:
                    archivo.write(f'{dato_bin},\n')

    def dec_a_bin(self, numero: int) -> str:
        return format(numero, f'0{self.ancho}b')

    def minmax(self, numero: int, minimo: int, maximo: int) -> int:
        if numero < minimo:
            return minimo
        elif numero > maximo:
            return maximo
        return numero


# Parametros
TAMANO_COE = 32
BITS_POR_NUMERO = 6
# Logica del programa
coegen = CoeGen(TAMANO_COE, BITS_POR_NUMERO)
print('Cantidad maxima de datos:', coegen.tamano)
try:
    cantidad = int(input('¿Cuantos datos desea ingresar?: '))
except ValueError as err:
    print('ERROR:', err)
    print('Definiendo cantidad como el tamaño del vector.')
    print('Cantidad definida en:', TAMANO_COE)
    cantidad = TAMANO_COE
i = 0
while i < cantidad:
    try:
        print('Maximo numero posible:', coegen.maximo)
        entrada = input('Ingresa un dato a añadir (decimal): ')
        entero = int(entrada)
        if entero > coegen.maximo:
            raise Exception('No puedes ingresar un numero mayor al máximo.')
        elif entero < 0:
            raise Exception('No puedes ingresar negativos.')
        coegen.datos.append(entero)
        i += 1
        print(f'Numeros ingresados hasta ahora: {i}/{cantidad}')
    except ValueError as error:
        print(f'ERROR: ingresa un numero entero válido. ({error})')
    except Exception as error:
        print('ERROR:', error)
coegen.generar_coe()
print('Archivo generado.')
input('Presiona cualquier tecla para continuar...')
