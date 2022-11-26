from parametros import INSTRUCCIONES, TAMANO_COE, BITS_POR_NUMERO, RUTA_COE, RUTA_PROGRAMA
from utils import minmax
from os.path import join
from collections import defaultdict


class Traductor:
    def __init__(self) -> None:
        self.tamano = minmax(TAMANO_COE, 16, 65536)
        self.ancho = minmax(BITS_POR_NUMERO, 1, 1024)
        self.instrucciones = []
        self.maximo = int(2**self.ancho) - 1

    def cargar_archivo(self):
        # Cargamos ruta del archivo
        lista_ruta = RUTA_PROGRAMA
        if type(lista_ruta) is list:
            ruta = join(*lista_ruta)
        else:
            ruta = lista_ruta
        # Leemos el archivo .txt
        n_linea = 0
        try:
            with open(ruta, mode='r', encoding='utf-8') as archivo:
                paso = 0
                for linea in archivo:
                    n_linea += 1
                    if linea[0] != '#' and linea != "\n":
                        paso += 1
                        linea_formateada = linea.strip()
                        self.instrucciones.append(
                            self.traducir_linea(linea_formateada))
                print(f'Instrucciones a procesar: {paso}')
            # Generamos .COE
            print('>> ¡Instrucciones procesadas! <<'.center(50, "-"))
            print('>> Generando archivo COE... <<'.center(50, "-"))
            self.generar_coe()
        except KeyError as error:
            print('ERROR'.center(50, "*"))
            print(f'Hay un error de escritura en la linea {n_linea}')
            print(f'Detalle: {error} no se reconoce como mnemotecnia.')

    def traducir_linea(self, linea: str) -> str:
        '''
        Traduce una linea de mnemotecnica a binario.
        '''
        datos = linea.split(' ')
        mnemo = datos[0]
        opcode = INSTRUCCIONES[mnemo][2]
        formato = INSTRUCCIONES[mnemo][1].split(',')

        d = defaultdict(lambda: "000")
        args = datos[1:]
        for i in range(len(formato)):
            if formato[i] == "RD":
                d[0] = self.int_a_bin(int(args[i]), 3)
            elif formato[i] == "RA":
                d[1] = self.int_a_bin(int(args[i]), 3)
            elif formato[i] in ["RB", "OP"]:
                d[2] = self.int_a_bin(int(args[i]), 3)
            elif formato[i] == "AD":
                AD = self.int_a_bin(int(args[i]), 6)
                d[0] = AD[:3]
                d[2] = AD[3:]

        return f'{opcode}{d[0]}{d[1]}{d[2]}'

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
                if len(self.instrucciones) > 0:
                    dato_bin = self.instrucciones.pop(0)
                else:
                    dato_bin = self.int_a_bin(-512, self.ancho)
                if i == (self.tamano - 1):
                    archivo.write(f'{dato_bin};')
                else:
                    archivo.write(f'{dato_bin},\n')
        print('>> ¡Archivo generado! <<'.center(50, "-"))

    def int_a_bin(self, numero: int, nbits: int) -> str:
        '''
        Formatea un numero entero a binario para su escritura
        '''
        negativo = numero < 0
        if negativo:
            # Conversion a complemento-2
            mag = format(numero * -1, f'0{nbits}b')
            magxy = mag.replace('0', 'x').replace('1', 'y')
            comp1 = int(magxy.replace('x', '1').replace('y', '0'), base=2)
            comp2 = format(comp1 + 1, f'0{nbits}b')
            return comp2
        return format(numero, f'0{nbits}b')
