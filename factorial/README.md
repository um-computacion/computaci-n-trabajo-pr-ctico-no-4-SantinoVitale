# Etapa 1: Factorial

## Descripción del problema
La función factorial de un número entero positivo `n` (denotado como `n!`) se define como el producto de todos los números enteros positivos desde 1 hasta `n`. Por definición, el factorial de 0 es 1.

Matemáticamente, para un entero `n ≥ 0`:
- `0! = 1`
- `n! = n × (n-1) × (n-2) × ... × 2 × 1`

Este problema puede resolverse tanto de forma iterativa como recursiva.

## Implementación
Se han desarrollado dos versiones de la función factorial:

1. **Versión Iterativa**: Utiliza un bucle para calcular el factorial.
2. **Versión Recursiva**: Se llama a sí misma con un parámetro más pequeño hasta alcanzar el caso base.

Ambas implementaciones incluyen manejo de casos especiales, como números negativos (para los cuales el factorial no está definido) y el caso particular de factorial de 0, que por definición es 1.

## Instrucciones de ejecución

### Para ejecutar los tests:
```bash
python test_factorial.py
```

### Para usar las funciones en su propio código:
```python
from factorial import factorial_iterativo, factorial_recursivo

# Ejemplos de uso
resultado_iterativo = factorial_iterativo(5)  # 120
resultado_recursivo = factorial_recursivo(5)  # 120
```

## Ejemplos de uso
```python
>>> from factorial import factorial_iterativo, factorial_recursivo
>>> factorial_iterativo(0)
1
>>> factorial_iterativo(5)
120
>>> factorial_recursivo(10)
3628800
>>> factorial_iterativo(-1)
Traceback (most recent call last):
  ...
ValueError: El factorial no está definido para números negativos
```

## Capturas de pantalla de los tests ejecutados
[Aquí se incluiría una captura de pantalla de los tests ejecutados exitosamente]