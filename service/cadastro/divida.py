

class DividaService():
	def __init__(self):
		#TODO O idial seria registrar informacoes em um DB
		# utilizando provalvelmente SQLAlchemy para mapeamento do objeto
		# Optei por utilizar um dicionario que ficará armazenado as informacoes
		# em cache, pois sera facil/rapido a insercao, atualizacao e exclusao

		# Caso fosse registrado informacoes em DB, poderiamos utilizar o
		# marshmallow, para efetuar a conversao do json em objeto para o Model

		self.divida_dict = {}

	def insert(self, divida_dict):
		self.__before_insert(divida_dict)

		if divida_dict['cpf'] not in self.divida_dict:
			self.divida_dict[divida_dict['cpf']] = {
				'nome': divida_dict['nome'],
				'cpf': divida_dict['cpf'],
				'valor': 0.0
			}

		self.divida_dict[divida_dict['cpf']]['valor'] += float(divida_dict['valor'])

	def __before_insert(self, divida_dict):
		self.__validate(divida_dict)

	def update(self, divida_dict):
		self.__before_update(divida_dict)
	
	def __before_update(self, divida_dict):
		self.__validate(divida_dict)

		self.divida_dict[divida_dict['cpf']].update(divida_dict)

	def delete(self, cpf):
		del(self.divida_dict[cpf])

	def __validate(self, divida_dict):
		if 'nome' not in divida_dict:
			raise DividaFieldRequiredException('Nome informacao obrigatoria')
		
		#TODO Deveria existir uma validacao de CPF
		if 'cpf' not in divida_dict:
			raise DividaFieldRequiredException('CPF informacao obrigatoria')

		if 'valor' not in divida_dict:
			raise DividaFieldRequiredException('Valor informacao obrigatoria')


class DividaFieldRequiredException(Exception):
	pass
