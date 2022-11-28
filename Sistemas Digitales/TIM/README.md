# TIM v1.1 (Traductor de Instrucciones de Memoria)
_Para python (versión recomendada: 3.10+)_

## Descripción
Este programa permite traducir instrucciones escritas en formato de ```mnemotecnicas``` a formato de ```opcode```. Para ello, se carga un archivo de texto con las instrucciones y es traducido al ejecutar el programa.

## ¿Cómo utilizar?
1. Descarga toda la carpeta en tu pc.
2. Ajustar los parametros editando ```parametros.py```. Algunas restricciones se aplican.
    > - **TAMANO_COE**: Indica el tamaño del vector. Este debe ser una potencia de 2 y el rango de valores válidos va desde **16** hasta **65536**. _Está configurado en **128** por defecto._
    > - **BITS_POR_NUMERO**: Indica la cantidad de bits de cada elemento, que va desde **1** hasta **1024**. _Está configurado en **16** por defecto._
    > - **RUTA_COE**: Ruta de salida del archivo ```.coe```.
    > - **VALOR_DEFAULT**: Valor por defecto para rellenar el archivo ```.coe``` para las lineas sin valor. Debe ser un ```string``` de largo ```BITS_POR_NUMERO```. Si se deja en blanco o se ingresa un valor con menos bits que ```BITS_POR_NUMERO```, el valor es rellenado con ```1```. _Está configurado en **''** por defecto._
    > - **RUTA_PROGRAMA**: Ruta de entrada del archivo ```.txt``` a traducir.
    > - **INSTRUCCIONES**: Instrucciones que procesa el traductor. Contiene los valores predeterminados y permite añadir mnemotecnias en el formato ```"MNEMO":   ["descripcion", "formato", "opcode"]```.
3. Escribir el programa en el archivo ```.txt``` dentro de la carpeta ```input```.
    > Se ha incluido un ejemplo de un programa dentro de la carpeta ```input```.
4. Ejecutar ```main.py```.
5. El archivo generado se encontrará en la carpeta ```output```.

## Ejemplo

### ```programa.txt```
```python
### ARCHIVO DE EJEMPLO ###
#
# Las lineas que comienzan con "#" (comentarios) y las lineas en blanco son
# ignoradas por el programa
#
# Instrucciones:
# 1- NO comentar en una linea de instruccion. Solo comenta en lineas
#    separadas del codigo
# 2- El formato de las instrucciones es mnemotecnica. Debes incluir
#    los argumentos minimos que requiere cada instruccion.
#
# FORMATO DE INSTRUCCION:   MNEMOTECNICA ARG1 ARG2 ARG3 ... ARGn
LD 0 0
MOVA 1 0
ADI 1 1 2
BRN 1 -2
ST 7 1
```

### ```datos.coe```
```
memory_initialization_radix = 2;
memory_initialization_vector =
0010000000000000,
0000000001000000,
1000010001001010,
1100001111001110,
0100000000111001,
1111111111111111,
1111111111111111,
⋮
1111111111111111;
```