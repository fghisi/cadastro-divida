import jwt
from jwt import ExpiredSignatureError

from datetime import datetime, timedelta


class Login():
	def __init__(self, usuario, senha):
		self.usuario = usuario
		self.senha = senha

	def valida_login(self):
		if self.usuario == 'admin' and self.senha == 'admin':
			return True

		return False

	def get_token(self):
		return JWTCD().get_jwt({
			"usuario": self.usuario,
		})


class JWTCD():

	def get_jwt(self, carga_dict):
		payload = {}
		for key, value in carga_dict.items():
			payload[key] = value

		payload['exp'] = self.__get_exp()

		return jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

	def validate(self, jwtcd):
		self.__get_decoded(jwtcd)

	def __get_decoded(self, jwtcd):
		try:
			return jwt.decode(jwtcd, 'secret')
		except ExpiredSignatureError:
			raise JWTCDExceptionExpired

	def __get_exp(self):
		return datetime.utcnow() + timedelta(hours=1)

class JWTCDExceptionExpired(Exception):
	pass
