# COEGEN
## ¿Cómo utilizar?
1. Descarga toda la carpeta en tu pc.
2. Ajustar los parametros editando ```parametros.py```. Algunas restricciones se aplican.
> **TAMANO_COE** indica el tamaño del vector. Este debe ser una potencia de 2 y el rango de valores válidos va desde **16** hasta **65536**. Por otro lado, **BITS_POR_NUMERO** indica la cantidad de bits de cada elemento, que va desde **1** hasta **1024**.
3. Ejecutar ```main.py```.
4. El programa inicialmente preguntará al usuario cuantos datos desea ingresar. El resto de los datos se rellenarán con **ceros**. El máximo de datos ingresable corresponde a **BITS_POR_NUMERO**.
5. Luego debes ingresar los números en formato **natural**, es decir, deben ser **enteros positivos**.
> Los datos son guardados en **magnitud sin signo**.

## Planes a futuro
Implementar selector de formato para numeros (Por ejemplo, complemento-2 y coma flotante de simple precisión)