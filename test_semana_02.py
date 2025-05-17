import unittest
from semana_02 import invertir_lista, collatz, contar_definiciones, cantidad_de_claves_letra, propagar


class TestInvertirLista(unittest.TestCase):
    def test_invertir_lista_vacia(self):
        self.assertEqual(invertir_lista([]), [])

    def test_invertir_lista_con_numeros(self):
        self.assertEqual(invertir_lista([1, 2, 3]), [3, 2, 1])
        self.assertEqual(invertir_lista([1, 2, 3, 2]), [2, 3, 2, 1])
    
    def test_invertir_lista_con_strings(self):
        self.assertEqual(invertir_lista(['Bogotá', 'Rosario', 'San Fernando', 'San Miguel']), ['San Miguel', 'San Fernando', 'Rosario', 'Bogotá'])
        self.assertEqual(invertir_lista(['a', 'b', 'c']), ['c', 'b', 'a'])

class TestCollatz(unittest.TestCase):
    def test_collatz(self):
        self.assertEqual(collatz(1), 0)
        self.assertEqual(collatz(2), 1)
        self.assertEqual(collatz(3), 7)

class TestContarDefiniciones(unittest.TestCase):
    def test_contar_definiciones(self):
        self.assertEqual(contar_definiciones({'a': [1, 2], 'b': [3]}), {'a': 2, 'b': 1})
    
    def test_contar_definiciones_vacio(self):
        self.assertEqual(contar_definiciones({}), {})
    
    def test_contar_definiciones_con_dicc_anidado(self):
        self.assertEqual(contar_definiciones({'a': [1, 2], 'b': [3], 'c': [{'d': 0, 'e':0}]}), {'a': 2, 'b': 1, 'c': 1})

class TestCantidadDeClavesLetra(unittest.TestCase):
    def test_cantidad_de_claves_letra(self):
        self.assertEqual(cantidad_de_claves_letra({'a': 1, 'b': 2, 'c': 3}, 'a'), 1)
        self.assertEqual(cantidad_de_claves_letra({'a': 1, 'b': 2, 'c': 3}, 'd'), 0)

    def test_cantidad_de_claves_letra_vacio(self):
        self.assertEqual(cantidad_de_claves_letra({}, 'a'), 0)

    def test_cantidad_de_claves_letra_mayuscula(self):
        self.assertEqual(cantidad_de_claves_letra({'a': 1, 'b': 2, 'c': 3}, 'A'), 1)

class TestPropagar(unittest.TestCase):
    def test_propagar(self):
        self.assertEqual(propagar([0, 0, 0, 1, 0, 0]), [1, 1, 1, 1, 1, 1])
        self.assertEqual(propagar([0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]), [0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1])
        self.assertEqual(propagar([0, 1, 0]), [1, 1, 1])

    def test_propagar_vacio(self):
        self.assertEqual(propagar([]), [])
    
    def test_propagar_todos_prendidos(self):
        self.assertEqual(propagar([1, 1, 1]), [1, 1, 1])
    
    def test_propagar_todos_apagados(self):
        self.assertEqual(propagar([0, 0, 0]), [0, 0, 0])


if __name__ == '__main__':
    unittest.main()