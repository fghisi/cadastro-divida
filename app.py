from bottle import Bottle

from controller.auth.login import app as login
from controller.cadastro.divida import app as divida

app = Bottle()
app.merge(login)
app.merge(divida)
app.run(host="0.0.0.0", port=8080)
