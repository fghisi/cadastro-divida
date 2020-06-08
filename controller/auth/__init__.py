import json
from bottle import request, response

from service.auth.login import JWTCD, JWTCDExceptionExpired


def validate_token(func):

	def validate(*args, **kwargs):
		token = request.headers.get('Authorization')

		if not token:
			response.status = 401
			return json.dumps({
				'mensagem': 'Token nao informado'
			})

		try:
			jwtcd = JWTCD()
			jwtcd.validate(token)

		except JWTCDExceptionExpired:
			response.status = 401
			return json.dumps({
				'mensagem': 'Token expirado'
			})

		return func(*args, **kwargs)

	return validate
