# Operadores de comparação
# As váriaveis username e password devem ser inseridas com os valores de 'admin' e '123456' respectivamente
# Ao iniciar o programa, serão solicitados o usuário e a senha
# Condições:
# Usuário e senha informados iguais ao usuário e senha da variável - Login efetuado com sucesso.
# Caso um dos campos informados esteja diferente - Usuário e/ou senha incorretos.

username = 'admin'
password = '123456'

input_user = input('Insira o usuário: ')
input_password = input('Insira a senha: ')

if input_user == username and input_password == password:
    print('Login efetuado com sucesso.')
else:
    print('Usuário e/ou senha incorretos.')