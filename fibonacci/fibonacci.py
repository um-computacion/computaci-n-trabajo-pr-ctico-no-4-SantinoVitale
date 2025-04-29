def fibonacci_iterativo(n):
  """
  Calcula el n-ésimo número de la secuencia de Fibonacci de forma iterativa.

  Args:
    n (int): La posición en la secuencia (comenzando desde 0).
        
  Returns:
    int: El n-ésimo número de Fibonacci.
        
  Raises:
    ValueError: Si n es un número negativo.
  """
  if n < 0:
    raise ValueError("La secuencia de Fibonacci no está definida para índices negativos")
    
  if n == 0:
    return 0
  if n == 1:
    return 1
    
  a, b = 0, 1
  for _ in range(2, n + 1):
    a, b = b, a + b
    
  return b

def fibonacci_recursivo(n):
  """
  Calcula el n-ésimo número de la secuencia de Fibonacci de forma recursiva.

  Args:
    n (int): La posición en la secuencia (comenzando desde 0).
        
  Returns:
    int: El n-ésimo número de Fibonacci.
        
  Raises:
    ValueError: Si n es un número negativo.
  """
  if n < 0:
    raise ValueError("La secuencia de Fibonacci no está definida para índices negativos")
    
  if n == 0:
    return 0
  if n == 1:
    return 1
    
  return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)