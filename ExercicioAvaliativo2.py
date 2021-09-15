#esse codigo foi desenvolvido para retornar ao usuario a criacao de um emai padrao da instituicao
# o email sera sempre a primeira letra do nome inserido  mais o sobrenome e os dois ultimos digitos da matricula

Nome = input('Escreva seu nome:')
Sobrenome = input('Escreva seu sobrenome:')
RU = int(input('Dois últimos número da matricula:'))
Mensagem = Nome + ' ' + Sobrenome

print('Sr {}, seu email é {}{}{}@algoritmos.com.br'.format(Mensagem,Nome[0], Sobrenome, RU))
