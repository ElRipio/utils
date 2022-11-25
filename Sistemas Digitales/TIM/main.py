from backend.coegen import CoeGen
from parametros import TAMANO_COE, BITS_POR_NUMERO


if __name__ == '__main__':
    coegen = CoeGen(TAMANO_COE, BITS_POR_NUMERO)
    print('>> TIM v1.0 <<'.center(50, '-'))
    print('>> Creado por: ElRipio <<'.center(50, '-'))
    print('-' * 50)
    print(' Parametros '.center(50, '-'))
    print(f'Tamaño del vector: {coegen.tamano}')
    print(f'Bits por número del vector: {coegen.ancho} bits')
    try:
        cantidad = int(input('¿Cuantos datos desea ingresar?: '))
    except ValueError as err:
        print(' ERROR '.center(50, '*'))
        print(err)
        print('Definiendo cantidad como el tamaño del vector.')
        print(f'Cantidad definida en: {coegen.tamano}')
        cantidad = coegen.tamano
    print(' Ingresar datos '.center(50, '-'))
    i = 0
    while i < cantidad:
        try:
            print('>>>> "CTRL + C" para detener ingreso de datos <<<<')
            print('Maximo numero posible:', coegen.maximo)
            entrada = input('Ingresa un número (natural): ')
            entero = int(entrada)
            if entero > coegen.maximo:
                raise Exception('Número supera al máximo.')
            elif entero < 0:
                raise Exception('No puedes ingresar negativos.')
            coegen.datos.append(entero)
            i += 1
            print(f'Numeros ingresados hasta ahora: {i}/{cantidad}')
        except KeyboardInterrupt:
            print('Interrumpiendo selección de números.')
            print(f'Tamaño final del vector: {i}')
            i = cantidad
        except ValueError as error:
            print(' ERROR '.center(50, '*'))
            print(f'ingresa un numero entero válido. ({error})')
        except Exception as error:
            print(' ERROR '.center(50, '*'))
            print(error)

    coegen.generar_coe()
    print('>> ¡Archivo generado! <<'.center(50, "-"))
    input('Presiona enter para terminar...')
