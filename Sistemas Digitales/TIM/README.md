# TIM v1.0 (Traductor de Instrucciones de Memoria)
_Para python (versión recomendada: 3.10+)_

## Descripción
Este programa permite traducir instrucciones escritas en formato de ```mnemotecnicas``` a formato de ```opcode```. Para ello, se carga un archivo de texto con las instrucciones y es traducido al ejecutar el programa.

## ¿Cómo utilizar?
1. Descarga toda la carpeta en tu pc.
2. Ajustar los parametros editando ```parametros.py```. Algunas restricciones se aplican.
    > - **TAMANO_COE**: indica el tamaño del vector. Este debe ser una potencia de 2 y el rango de valores válidos va desde **16** hasta **65536**. _Está configurado en **128** por defecto._
    > - **BITS_POR_NUMERO**: indica la cantidad de bits de cada elemento, que va desde **1** hasta **1024**. _Está configurado en **16** por defecto._
    > - **RUTA_COE**: Ruta de salida del archivo ```.coe```.
    > - **RUTA_PROGRAMA**: Ruta de entrada del archivo ```.txt``` a traducir.
    > - **INSTRUCCIONES**: Instrucciones que procesa el traductor. Contiene los valores predeterminados y permite añadir mnemotecnias.
3. Escribir el programa en el archivo ```.txt``` dentro de la carpeta output.
    > Se ha incluido un ejemplo de un programa dentro de la carpeta ```input```.
4. Ejecutar ```main.py```.
5. El archivo generado se encontrará en la carpeta ```output```.