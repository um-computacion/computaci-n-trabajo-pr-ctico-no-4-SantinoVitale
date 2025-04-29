# Etapa 3: Aplanar Listas

## Descripción del problema
El problema consiste en implementar una función recursiva que tome una estructura de datos anidada (como listas dentro de listas, tuplas, diccionarios, etc.) y devuelva una lista plana que contenga todos los elementos primitivos en un solo nivel.

Por ejemplo, una lista como `[1, [2, 3], [4, [5, 6]]]` debe convertirse en `[1, 2, 3, 4, 5, 6]`.

## Implementación
Se ha desarrollado una función recursiva `flatten` que puede manejar diferentes tipos de estructuras de datos anidadas:

1. Listas y tuplas anidadas
2. Diccionarios (incluyendo tanto claves como valores)
3. Tipos primitivos (enteros, flotantes, cadenas, booleanos, None)

La implementación utiliza recursividad para navegar a través de las estructuras anidadas y extraer cada elemento primitivo.

## Instrucciones de ejecución

### Para ejecutar los tests:
```bash
python test_flatten.py
```

### Para usar la función en su propio código:
```python
from flatten import flatten

# Ejemplos de uso
lista_anidada = [1, [2, 3], [4, [5, 6]]]
resultado = flatten(lista_anidada)  # [1, 2, 3, 4, 5, 6]
```

## Ejemplos de uso
```python
>>> from flatten import flatten
>>> flatten([1, 2, 3, 4])
[1, 2, 3, 4]
>>> flatten([1, [2, 3], [4, [5, 6]]])
[1, 2, 3, 4, 5, 6]
>>> flatten([1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]])
[1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
>>> flatten({'a': [1, 2], 'b': 3})
['a', 1, 2, 'b', 3]
```

## Funcionalidades soportadas
- Aplanar listas simples
- Aplanar listas con listas anidadas
- Aplanar estructuras mixtas (listas, tuplas, diccionarios)
- Manejo correcto de tipos primitivos

## Capturas de pantalla de los tests ejecutados
[Aquí se incluiría una captura de pantalla de los tests ejecutados exitosamente]