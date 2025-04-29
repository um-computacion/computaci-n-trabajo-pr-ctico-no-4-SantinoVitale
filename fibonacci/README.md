# Etapa 2: Fibonacci

## Descripción del problema
La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores. Por convención, los dos primeros números de la secuencia son 0 y 1.

Matemáticamente, para un entero `n ≥ 0`:
- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n-1) + F(n-2)` para `n > 1`

Este problema puede resolverse tanto de forma iterativa como recursiva.

## Implementación
Se han desarrollado dos versiones de la función Fibonacci:

1. **Versión Iterativa**: Utiliza un bucle para calcular el n-ésimo número de Fibonacci.
2. **Versión Recursiva**: Se llama a sí misma con parámetros más pequeños hasta alcanzar los casos base.

Ambas implementaciones incluyen manejo de casos especiales, como índices negativos (para los cuales la secuencia no está definida) y los casos particulares de los índices 0 y 1, cuyos valores son 0 y 1 respectivamente.

## Instrucciones de ejecución

### Para ejecutar los tests:
```bash
python test_fibonacci.py
```

### Para usar las funciones en su propio código:
```python
from fibonacci import fibonacci_iterativo, fibonacci_recursivo

# Ejemplos de uso
resultado_iterativo = fibonacci_iterativo(6)  # 8
resultado_recursivo = fibonacci_recursivo(6)  # 8
```

## Ejemplos de uso
```python
>>> from fibonacci import fibonacci_iterativo, fibonacci_recursivo
>>> fibonacci_iterativo(0)
0
>>> fibonacci_iterativo(1)
1
>>> fibonacci_iterativo(6)
8
>>> fibonacci_recursivo(10)
55
>>> fibonacci_iterativo(-1)
Traceback (most recent call last):
  ...
ValueError: La secuencia de Fibonacci no está definida para índices negativos
```

## Observaciones importantes
La implementación recursiva de Fibonacci tiene una complejidad temporal exponencial (O(2^n)), lo que la hace muy ineficiente para valores grandes de n. Por esta razón, se recomienda usar la versión iterativa (O(n)) para casos prácticos.

## Capturas de pantalla de los tests ejecutados
[Aquí se incluiría una captura de pantalla de los tests ejecutados exitosamente]