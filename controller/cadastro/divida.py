import json

from bottle import Bottle, request, response

from service.cadastro.divida import DividaService, DividaFieldRequiredException

from controller.auth import validate_token

app = Bottle()
divida_service = DividaService()

@app.route('/dividas', method='POST')
@validate_token
def post_divida():
	divida_dict = request.json

	try:
		divida_service.insert(divida_dict)
	
		response.status = 200
		return json.dumps({
			'mensagem': 'Divida registrada'
		})
	
	except DividaFieldRequiredException as e:
		response.status = 401
		return json.dumps({
			'mensagem': e.__str__()
		})


@app.route('/dividas/<cpf>', method='PUT')
@validate_token
def put_divida(cpf):
	if not divida_service.divida_dict.get(cpf):
		response.status = 404
		return json.dumps({
			'mensagem': 'Nao foi encontrada divida para CPF informado'
		})
	
	divida_dict = request.json
	divida_dict['cpf'] = cpf

	try:
		divida_service.update(divida_dict)
	
		response.status = 200
		return json.dumps({
			'mensagem': 'Divida atualizada'
		})
	
	except DividaFieldRequiredException as e:
		response.status = 401
		return json.dumps({
			'mensagem': e.__str__()
		})


@app.route('/dividas/<cpf>', method='DELETE')
@validate_token
def delete_divida(cpf):
	if not divida_service.divida_dict.get(cpf):
		response.status = 404
		return json.dumps({
			'mensagem': 'Nao foi encontrada divida para CPF informado'
		})
	
	divida_service.delete(cpf)
	response.status = 200
	return json.dumps({
		'mensagem': 'Divida excluida'
	})

@app.route('/dividas/<cpf>', method='GET')
def get_dividas(cpf):
	info_dict = divida_service.divida_dict.get(cpf)

	if not info_dict:
		response.status = 404
		return json.dumps({
			'mensagem': 'Nao foi encontrada divida para CPF informado'
		})

	response.status = 200
	return json.dumps(info_dict)
