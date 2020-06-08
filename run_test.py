from unittest import TestLoader, TextTestRunner

pattern = '*test.py'
base_test = 'test'

test_modules = [
	'service/auth',
	'service/cadastro'
]

for module in test_modules:
	suite = TestLoader().discover('%s/%s' % (base_test, module), pattern)
	runner = TextTestRunner(verbosity=1)
	runner.run(suite)
