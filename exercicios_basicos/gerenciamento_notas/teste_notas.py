import unittest
import gerenciador_notas

class TesteNotas (unittest.TestCase):


    def test_condicoes_normais(self):
        self.assertEqual(gerenciador_notas.verificar_aprovacao(6.0, media_minima=7), "Reprovado")

    def test_lista_vazia (self):
        notas = []
        self.assertEqual(gerenciador_notas.calcular_media(notas), 0)

    def test_media_zero(self):
        self.assertEqual(gerenciador_notas.verificar_aprovacao(5.4, media_minima=0), "Aprovado")

if __name__ == '__main__':
    unittest.main()

# condições normais de aprovação e reprovação

# teste do caso extremo com a lista de notas vazia

# acionamento limitador da função informando zero na média de corte
