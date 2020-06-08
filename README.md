# Cadastro de Dívidas 

## Criando ambiente

Criar um ambiente virtual para isolamento da versão do python e suas dependências.

```sh
python3.8 -m venv .env
```

```sh
# ativar o ambiente virtual
source .env/bin/activate

# e para desativar
deactivate
```

Gerenciando as dependências através do pip.

```
pip install -r requirements.txt
```

## Consumindo a API

Uma API para cadastro e consulta de dívidas de pessoas fisícas.

Foram criados os recursos abaixo:
- "/login" - Usuario = admin e senha = admin por padrao
- "/dividas" - Metodo POST para inserir dividas de uma pessoa fisica, passando sempre o token de autorizacao
- "/dividas/<cpf>" - Metodo PUT e DELETE para atualizar e excluir dividas de uma pessoa fisica, passando sempre o token
- "/dividas/<cpf>" - Metodo GET sem necessidade de token, para utilizacao de consulta de dividas por CPF
