import unittest

from service.cadastro.divida import DividaService, DividaFieldRequiredException


class DividaServiceTest(unittest.TestCase):

	def setUp(self):
		self.divida_service = DividaService()

	def test_validate_divida(self):

		info_dict = {'nome': 'Joao', 'valor': 100}
		with self.assertRaises(DividaFieldRequiredException, msg='Inserido divida sem campos requeridos'):
			self.divida_service._DividaService__validate(info_dict)

		info_dict = {'cpf': '71833011414', 'valor': 100}
		with self.assertRaises(DividaFieldRequiredException, msg='Inserido divida sem campos requeridos'):
			self.divida_service._DividaService__validate(info_dict)

		info_dict = {'cpf': '71833011414', 'nome': 'Joao'}
		with self.assertRaises(DividaFieldRequiredException, msg='Inserido divida sem campos requeridos'):
			self.divida_service._DividaService__validate(info_dict)

	def test_insert_divida(self):
		info_dict = {'cpf': '71833011414', 'nome': 'Joao', 'valor': 100}
		self.divida_service.insert(info_dict)

		self.assertEqual(self.divida_service.divida_dict['71833011414']['cpf'], '71833011414', 'Nao foi inserido divida')
		self.assertEqual(self.divida_service.divida_dict['71833011414']['nome'], 'Joao', 'Nao foi inserido divida')
		self.assertEqual(self.divida_service.divida_dict['71833011414']['valor'], 100, 'Nao foi inserido divida')

		info_dict = {'cpf': '71833011414', 'nome': 'Joao', 'valor': 10}
		self.divida_service.insert(info_dict)
		self.assertEqual(self.divida_service.divida_dict['71833011414']['valor'], 110, 'Nao foi somado o valor da divida')

	def test_update_divida(self):
		info_dict = {'cpf': '71833011414', 'nome': 'Joao', 'valor': 100}
		self.divida_service.insert(info_dict)
		
		info_dict = {'cpf': '71833011414', 'nome': 'Joao', 'valor': 10}
		self.divida_service.update(info_dict)
		
		self.assertEqual(self.divida_service.divida_dict['71833011414']['valor'], 10, 'Nao foi atualizado o valor da divida')



if __name__ == '__main__':
	unittest.main()
