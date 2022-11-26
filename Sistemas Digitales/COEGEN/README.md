# COEGEN v1.1 (Generador de archivos COE)
_Para python (versión recomendada: 3.10+)_

## Descripción
Este programa permite generar archivos ```.coe``` para instanciar memorias en vivado, mediante el ingreso de datos por consola.

## ¿Cómo utilizar?
1. Descarga toda la carpeta en tu pc.
2. Ajustar los parametros editando ```parametros.py```. Algunas restricciones se aplican.
> - **TAMANO_COE**: indica el tamaño del vector. Este debe ser una potencia de 2 y el rango de valores válidos va desde **16** hasta **65536**. _Está configurado en **32** por defecto._
> - **BITS_POR_NUMERO**: indica la cantidad de bits de cada elemento, que va desde **1** hasta **1024**. _Está configurado en **8** por defecto._
> - **RUTA_COE**: Ruta de salida del archivo ```.coe```.
3. Ejecutar ```main.py```.
4. El programa inicialmente preguntará al usuario cuantos datos desea ingresar. El resto de los datos se rellenarán con **ceros**. El máximo de datos ingresable corresponde a **TAMANO_COE**.
5. Luego debes ingresar los **números enteros** que deseas guardar en el archivo.
> Los datos son guardados en **complemento 2**.

## Planes a futuro
Implementar formato para numeros decimales (Por ejemplo, coma flotante de simple precisión).