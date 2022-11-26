from traductor import Traductor


if __name__ == '__main__':
    traductor = Traductor()
    print('=' * 50)
    print('>> TIM v1.0 <<'.center(50, '-'))
    print('>> Creado por: ElRipio <<'.center(50, '-'))
    print('=' * 50)
    print(' Parametros '.center(50, '~'))
    print(f'Tamaño del vector: {traductor.tamano}')
    print(f'Bits por número del vector: {traductor.ancho} bits')
    print(' Traduciendo programa '.center(50, '-'))
    traductor.cargar_archivo()
    input('Presiona enter para terminar...')
