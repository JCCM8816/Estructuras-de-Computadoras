# Estructuras-de-Computadoras - Tarea # 1
# Comportamiento de una Memoria Cache
El programa Cache.py permite simulñar el comportamiento de una memoria cache y encontrar tanto la cantidad de hits como de misses obtenidos al utilizar las direcciones que se encuentran en el archivo aligned.trace. La memoria cache esta diseñada para realizar No-write allocate, write through y reemplazo aleatorio.

## Modo de Uso
El programa recibe tres argumetos: 
* **Asociatividad** : Puede ser Directo (`Directo`), 2-way Asociativity (`2-way`), 4-way Asociativity (`4-way`)
* **Tamaño de Cache**: Tiene que ser un numero de la forma 2^n, n=0,1,2,3,...
* **Tamaño de Bloque**: Tiene que ser un numero de la forma 2^n, n=0,1,2,3,...

De esta forma para correr el programa es necesario utilizar la siguiente sintaxis:

`python Cache.py <Asociatividad> <Tamaño de Cache> <Tamaño de Bloque>`

Ejemplo: `python Cache.py 4-way 4096 36`

Nota: El archivo aligned.trace debe de estar en la misma carpeta que Cache.py para evitar errores.

