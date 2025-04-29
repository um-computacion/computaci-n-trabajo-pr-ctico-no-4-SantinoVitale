def factorial_iterativo(n):
  """
  Calcula el factorial de un número de forma iterativa.

  Args:
    n (int): El número para calcular su factorial.
        
  Returns:
    int: El factorial de n.
        
  Raises:
    ValueError: Si n es un número negativo.
  """
  if n < 0:
    raise ValueError("El factorial no está definido para números negativos")
    
  resultado = 1
  for i in range(1, n + 1):
    resultado *= i
    
  return resultado

def factorial_recursivo(n):
  """
  Calcula el factorial de un número de forma recursiva.

  Args:
    n (int): El número para calcular su factorial.

  Returns:
    int: El factorial de n.
        
  Raises:
    ValueError: Si n es un número negativo.
  """
  if n < 0:
    raise ValueError("El factorial no está definido para números negativos")
    
  if n == 0 or n == 1:
    return 1
    
  return n * factorial_recursivo(n - 1)