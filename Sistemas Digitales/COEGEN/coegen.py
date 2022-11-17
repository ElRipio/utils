'''
Módulo que contiene la clase CoeGen del programa.
'''

from parametros import RUTA_COE
from os.path import join


class CoeGen:
    def __init__(self, tamano: int = 16, ancho: int = 8) -> None:
        self.datos = []
        self.tamano = self.minmax(tamano, 16, 65536)
        self.ancho = self.minmax(ancho, 1, 1024)
        self.maximo = int(2**self.ancho) - 1

    def generar_coe(self):
        # Cargamos ruta del archivo
        lista_ruta = RUTA_COE
        if type(lista_ruta) is list:
            ruta = join(*lista_ruta)
        else:
            ruta = lista_ruta
        # Escribimos el archivo .coe
        with open(ruta, mode='w', encoding='utf-8') as archivo:
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
        '''
        Formatea un numero decimal a binario para su escritura
        '''
        return format(numero, f'0{self.ancho}b')

    def minmax(self, numero: int, minimo: int, maximo: int) -> int:
        '''
        "Encierra" un valor entre un mínimo y un máximo.
        '''
        if numero < minimo:
            return minimo
        elif numero > maximo:
            return maximo
        return numero
