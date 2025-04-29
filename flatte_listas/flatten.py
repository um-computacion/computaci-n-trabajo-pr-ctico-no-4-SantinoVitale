def flatten(estructura):
  """
  Aplana una estructura de datos anidada (listas, tuplas, diccionarios) en una lista simple.

  Args:
    estructura: La estructura de datos a aplanar. Puede ser una lista, tupla, 
    diccionario o una combinación anidada de estos tipos.
        
  Returns:
    list: Una lista aplanada que contiene todos los elementos primitivos de la estructura.
  """
  result = []
    
  # Caso base: Si el elemento es un tipo primitivo, lo añadimos directamente
  if isinstance(estructura, (int, float, str, bool, type(None))):
    return [estructura]
    
  # Si es un diccionario, aplanamos las claves y los valores
  elif isinstance(estructura, dict):
    for key, value in estructura.items():
      result.extend(flatten(key))
      result.extend(flatten(value))
    
  # Si es una lista o tupla, aplanamos cada elemento
  elif isinstance(estructura, (list, tuple)):
    for item in estructura:
      result.extend(flatten(item))
    
  # Para cualquier otro tipo, lo tratamos como un elemento primitivo
  else:
    result.append(estructura)
    
  return result