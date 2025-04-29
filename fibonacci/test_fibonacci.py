import unittest
from fibonacci import fibonacci_iterativo, fibonacci_recursivo

class TestFibonacci(unittest.TestCase):
  """Clase para probar las implementaciones de Fibonacci."""
    
  def test_fibonacci_iterativo_casos_base(self):
    """Prueba casos base para la implementación iterativa."""
    self.assertEqual(fibonacci_iterativo(0), 0)
    self.assertEqual(fibonacci_iterativo(1), 1)
    
  def test_fibonacci_iterativo_casos_normales(self):
    """Prueba casos normales para la implementación iterativa."""
    self.assertEqual(fibonacci_iterativo(2), 1)
    self.assertEqual(fibonacci_iterativo(3), 2)
    self.assertEqual(fibonacci_iterativo(4), 3)
    self.assertEqual(fibonacci_iterativo(5), 5)
    self.assertEqual(fibonacci_iterativo(6), 8)
    self.assertEqual(fibonacci_iterativo(10), 55)
    
  def test_fibonacci_iterativo_casos_especiales(self):
    """Prueba casos especiales para la implementación iterativa."""
    with self.assertRaises(ValueError):
      fibonacci_iterativo(-1)
    with self.assertRaises(ValueError):
      fibonacci_iterativo(-10)
    
  def test_fibonacci_recursivo_casos_base(self):
    """Prueba casos base para la implementación recursiva."""
    self.assertEqual(fibonacci_recursivo(0), 0)
    self.assertEqual(fibonacci_recursivo(1), 1)
    
  def test_fibonacci_recursivo_casos_normales(self):
    """Prueba casos normales para la implementación recursiva."""
    self.assertEqual(fibonacci_recursivo(2), 1)
    self.assertEqual(fibonacci_recursivo(3), 2)
    self.assertEqual(fibonacci_recursivo(4), 3)
    self.assertEqual(fibonacci_recursivo(5), 5)
    self.assertEqual(fibonacci_recursivo(6), 8)
    self.assertEqual(fibonacci_recursivo(10), 55)
    
  def test_fibonacci_recursivo_casos_especiales(self):
    """Prueba casos especiales para la implementación recursiva."""
    with self.assertRaises(ValueError):
      fibonacci_recursivo(-1)
    with self.assertRaises(ValueError):
      fibonacci_recursivo(-10)
    
  def test_ambas_implementaciones_producen_resultados_iguales(self):
    """Verifica que ambas implementaciones producen los mismos resultados."""
    # Nota: Limitamos a valores pequeños porque la versión recursiva es ineficiente
    for n in range(15):  # Probar con números del 0 al 14
      self.assertEqual(fibonacci_iterativo(n), fibonacci_recursivo(n))

if __name__ == '__main__':
  unittest.main()