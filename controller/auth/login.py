import json

from bottle import Bottle, request, response

from service.auth.login import Login

app = Bottle()


@app.route('/login', method='POST')
def login():
	usuario = request.json.get('usuario')
	senha = request.json.get('senha')

	if not usuario or not senha:
		response.status = 400
		return json.dumps({
			'mensagem': 'Usuario ou senha nao informado'
		})

	login = Login(usuario, senha)

	if not login.valida_login():
		response.status = 401
		return json.dumps({
			'mensagem': 'Requisicao nao autorizada'
		})

	return json.dumps({
		'token': str(login.get_token()),
		'mensagem': 'Login efetuado com sucesso'
	})

