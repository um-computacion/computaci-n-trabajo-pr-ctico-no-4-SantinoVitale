import unittest
from factorial import factorial_iterativo, factorial_recursivo

class TestFactorial(unittest.TestCase):
  """Clase para probar las implementaciones de factorial."""
    
  def test_factorial_iterativo_casos_base(self):
    """Prueba casos base para la implementación iterativa."""
    self.assertEqual(factorial_iterativo(0), 1)
    self.assertEqual(factorial_iterativo(1), 1)
    
  def test_factorial_iterativo_casos_normales(self):
    """Prueba casos normales para la implementación iterativa."""
    self.assertEqual(factorial_iterativo(2), 2)
    self.assertEqual(factorial_iterativo(3), 6)
    self.assertEqual(factorial_iterativo(5), 120)
    self.assertEqual(factorial_iterativo(10), 3628800)
    
  def test_factorial_iterativo_casos_especiales(self):
    """Prueba casos especiales para la implementación iterativa."""
    with self.assertRaises(ValueError):
      factorial_iterativo(-1)
    with self.assertRaises(ValueError):
      factorial_iterativo(-10)
    
  def test_factorial_recursivo_casos_base(self):
    """Prueba casos base para la implementación recursiva."""
    self.assertEqual(factorial_recursivo(0), 1)
    self.assertEqual(factorial_recursivo(1), 1)
    
  def test_factorial_recursivo_casos_normales(self):
    """Prueba casos normales para la implementación recursiva."""
    self.assertEqual(factorial_recursivo(2), 2)
    self.assertEqual(factorial_recursivo(3), 6)
    self.assertEqual(factorial_recursivo(5), 120)
    self.assertEqual(factorial_recursivo(10), 3628800)
    
  def test_factorial_recursivo_casos_especiales(self):
    """Prueba casos especiales para la implementación recursiva."""
    with self.assertRaises(ValueError):
      factorial_recursivo(-1)
    with self.assertRaises(ValueError):
      factorial_recursivo(-10)
    
  def test_ambas_implementaciones_producen_resultados_iguales(self):
    """Verifica que ambas implementaciones producen los mismos resultados."""
    for n in range(20):  # Probar con números del 0 al 19
      self.assertEqual(factorial_iterativo(n), factorial_recursivo(n))

if __name__ == '__main__':
  unittest.main()