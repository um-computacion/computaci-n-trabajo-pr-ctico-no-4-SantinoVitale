import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):
  """Clase para probar la implementación de la función flatten."""
    
  def test_lista_simple(self):
    """Prueba con una lista simple."""
    lista = [1, 2, 3, 4]
    resultado_esperado = [1, 2, 3, 4]
    self.assertEqual(flatten(lista), resultado_esperado)
    
  def test_lista_con_listas_anidadas(self):
    """Prueba con una lista que contiene listas anidadas."""
    lista = [1, [2, 3], [4, [5, 6]]]
    resultado_esperado = [1, 2, 3, 4, 5, 6]
    self.assertEqual(flatten(lista), resultado_esperado)
    
  def test_lista_con_diferentes_estructuras(self):
    """Prueba con una lista que contiene diferentes tipos de estructuras."""
    lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
    resultado_esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
    self.assertEqual(flatten(lista), resultado_esperado)
    
  def test_lista_vacia(self):
    """Prueba con una lista vacía."""
    lista = []
    resultado_esperado = []
    self.assertEqual(flatten(lista), resultado_esperado)
    
  def test_diccionario_simple(self):
    """Prueba con un diccionario simple."""
    diccionario = {'a': 1, 'b': 2}
    resultado_esperado = ['a', 1, 'b', 2]
    self.assertEqual(flatten(diccionario), resultado_esperado)
    
  def test_tupla_simple(self):
    """Prueba con una tupla simple."""
    tupla = (1, 2, 3)
    resultado_esperado = [1, 2, 3]
    self.assertEqual(flatten(tupla), resultado_esperado)
    
  def test_estructura_compleja(self):
    """Prueba con una estructura compleja."""
    estructura = [
      1, 
      (2, 3), 
      {'a': [4, 5], 'b': {'c': 6, 'd': (7, 8)}},
      [9, [10, {'e': 11}]]
    ]
    resultado_esperado = [1, 2, 3, 'a', 4, 5, 'b', 'c', 6, 'd', 7, 8, 9, 10, 'e', 11]
    self.assertEqual(flatten(estructura), resultado_esperado)
    
  def test_tipos_primitivos(self):
    """Prueba con tipos primitivos."""
    self.assertEqual(flatten(42), [42])
    self.assertEqual(flatten("hola"), ["hola"])
    self.assertEqual(flatten(True), [True])
    self.assertEqual(flatten(None), [None])

if __name__ == '__main__':
  unittest.main()