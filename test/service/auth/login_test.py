import unittest

from service.auth.login import Login


class LoginTest(unittest.TestCase):

	def test_login_valido(self):
		login = Login('admin', 'admin')

		result = login.valida_login()
		self.assertEqual(result, True, msg='Nao conseguiu efetuar login')
	
	def test_login_senha_invalida(self):
		login = Login('admin', 'adminn')

		result = login.valida_login()
		self.assertEqual(result, False, msg='Conseguiu efetuar login com senha invalida')

	def test_login_usuario_invalido(self):
		login = Login('adminn', 'admin')

		result = login.valida_login()
		self.assertEqual(result, False, msg='Conseguiu efetuar login com usuario invalido')

if __name__ == '__main__':
	unittest.main()
