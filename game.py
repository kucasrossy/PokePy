from pokemon import *
from trainner import *

trainner_enemy = Trainner('Edilson', 3, [Bulbassauro("Verde", 10), Bulbassauro('Verde mais Escuro', 15), Charmander('Vermelho',5)])

jogar = False

print(75*'-')
print(25*' ' + 'Bem vindo a PokePy')
print(75*'-')
print('Eu sou o Dr Irineu, e hoje eu entregarei o seus pokemons')
nome = input('Mas primeiro qual é o seu nome?\n')
print('É um prazer de conhecer {}, vamos começar então, escolhar o seu pokemom: '.format(nome))
escolhar = int(input('1: Charmander 2:Bulbassauro 3:Squirtle\n'))
while escolhar < 1 or escolhar > 3:
    escolhar = int(input('Meu querido eu só tenho essas três opções, por favor escolhar entre elas\n'))

if escolhar == 1:
    print('Muito bem você escolheu o Charmander')
    nome_pok = input('Qual vai ser o nome dele?\n')
    print('o seu {} vai começa no level 5, esteja preparado para o pior\nBjs'.format(nome_pok))
elif escolhar == 2:
    print('Muito bem você escolheu o Bulbassauro')
    nome_pok = input('Qual vai ser o nome dele?\n')
    print('o seu {} vai começa no level 5, esteja preparado para o pior\nBjs'.format(nome_pok))
else:
    print('Muito bem você escolheu o Squirtle')
    nome_pok = input('Qual vai ser o nome dele?\n')
    print('o seu {} vai começa no level 5, esteja preparado para o pior\nBjs'.format(nome_pok))



while jogar: 
    pass